document.addEventListener('DOMContentLoaded', function() {
    const dropdowns = document.querySelectorAll('.dropdown');

    dropdowns.forEach(dropdown => {
        const content = dropdown.querySelector('.dropdown-content');
        let timeout;

        // Функция за десктоп (mouseenter)
        dropdown.addEventListener('mouseenter', function() {
            // Активираме само ако екрана е над 768px (десктоп)
            if (window.innerWidth > 768) {
                clearTimeout(timeout);
                content.classList.add('show');
            }
        });

        // Функция за десктоп (mouseleave)
        dropdown.addEventListener('mouseleave', function() {
            if (window.innerWidth > 768) {
                timeout = setTimeout(() => {
                    content.classList.remove('show');
                }, 500); 
            }
        });

        // ПРЕМАХВАМЕ всякакви click събития, които пречат на линка
        // Сега на мобилен, когато цъкнеш на "Locations", 
        // браузърът просто ще те отведе на адреса в href=""
    });
});
let currentPage = 1;
async function handlePagination(page) {
    const urlParams = new URLSearchParams(window.location.search);
    const type = urlParams.get('type') || '';

    try {
        const response = await fetch(`?page=${page}&type=${type}`,{
            headers: { 'x-requested-with': 'XMLHttpRequest' }
        });

        if (!response.ok) throw new Error('Network response was not ok!');
        const data = await response.json();
        
        const parser = new DOMParser();
        const doc = parser.parseFromString(data.html, 'text/html');
        const newPlaces = doc.getElementById('places-anchor').innerHTML;

        document.getElementById('places-anchor').innerHTML = newPlaces;
        document.getElementById('pageCounter').innerText = `Page ${data.page}`;

        currentPage = data.page;
        
        document.getElementById('prevBtn').style.display = data.previous_page ? 'inline-block' : 'none';
        document.getElementById('nextBtn').style.display = data.next_page ? 'inline-block' : 'none';
        document.getElementById('places-anchor').scrollIntoView({ behavior: 'smooth' });

    } catch (error) {
        console.error("Error with reloading at pages:", error);
    }
}

document.addEventListener('DOMContentLoaded', () => {
    const nextBtn = document.getElementById('nextBtn');
    const prevBtn = document.getElementById('prevBtn');

    if (nextBtn && prevBtn) {
        nextBtn.addEventListener('click', () => handlePagination(currentPage + 1));
        prevBtn.addEventListener('click', () => handlePagination(currentPage - 1));
    }
});