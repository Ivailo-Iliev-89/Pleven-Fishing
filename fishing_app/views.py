from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.db.models import Q
from django.core.paginator import Paginator
from django.template.loader import render_to_string
from django.http import JsonResponse
from blog.forms import ReportPostForm
from .models import FishingPlace, Method
from .utils import get_weather_data
import random


# TODO
# разделя локациите от метода (за лаптоп едното в ляво другото в дянсо ( в средата ще видим ),
# и ховър жълто на текста
# И направата на изцяло нови хтмл-и за локации и реките, може би..(ако не още малко и да го пусна)
# Но да направя и секция за коментари във постовете и реплайове(от блог поста ми)

# The home page
def index(request):
    places = FishingPlace.objects.all().order_by('name')
    place_type = request.GET.get('type')

    if place_type:
        places = places.filter(place_type__iexact=place_type)

    paginator = Paginator(places, 3)  # Show 3 locations at one page
    page_number = request.GET.get('page', 1)
    places = paginator.get_page(page_number)

    # AJAX request to insert peace of code with innerHTML
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        html = render_to_string('fishing_app/index.html',
                                {'places': places}, request=request)
        next_page = places.has_next()
        previous_page = places.has_previous()
        page = places.number

        return JsonResponse({
            'html': html,
            'next_page': next_page,
            'previous_page': previous_page,
            'page': page
        })

    return render(request, 'fishing_app/index.html', {
        'places': places,
        'selected_type': place_type
    })


# Detail for current location( for example - Vit River)
def place_detail(request, slug):
    place = get_object_or_404(FishingPlace, slug=slug)
    # Show Weather from API
    weather = None
    if place.latitude and place.longitude:
        weather = get_weather_data(place.latitude, place.longitude)

    # Show ReportPostForm from database to user
    posts = place.posts.filter(status='1').order_by('-created_on')
    if request.method == 'POST':
        form = ReportPostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.location = place
            new_post.author = request.user
            new_post.status = '1'
            new_post.save()
            return redirect('place_detail', slug=slug)
    else:
        form = ReportPostForm()

    return render(request, 'fishing_app/place_detail.html', {
        'place': place,
        'posts': posts,
        'form': form,
        'weather': weather
    })


# Filter by methods of fishing
def method_detail(request, slug):
    method = get_object_or_404(Method, slug=slug)
    places = method.places.all()
    return render(request, 'fishing_app/method_filter.html', {
        'method': method,
        'places': places
    })


# Filter by types of locations
def type_filter(request, place_type):
    places = FishingPlace.objects.filter(place_type=place_type)
    type_name = dict(FishingPlace.PLACE_TYPES).get(place_type)
    return render(request, 'fishing_app/type_filter.html', {
        'places': places,
        'type_name': type_name
    })


# About Section at Footer
def about(request):
    return render(request, 'fishing_app/about.html')


# Advices Section at Footer
def advices(request):
    return render(request, 'fishing_app/advices.html')


# Login/Register
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm
        if form.is_valid:
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm

    return render(request, 'registration/signup.html', {'form': form})


# Discover Page at Hero Section
def discover(request):
    all_places = list(FishingPlace.objects.all())
    recommended_places = random.sample(all_places, min(len(all_places), 3))

    return render(request, 'fishing_app/discover.html', {'recommended': recommended_places})


# Search Results at Discover Page
def search_results(request):
    query = request.GET.get('q', '').strip()
    results = []

    if query:
        results = FishingPlace.objects.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(fishes__name__icontains=query) |
            Q(methods__name__icontains=query)
        ).distinct()
    return render(request, 'fishing_app/search_results.html', {
        'results': results,
        'query': query
    })
