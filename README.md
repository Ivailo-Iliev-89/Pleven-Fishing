# PlevenFishing Atlas
A Full-Stack Geospatial Directory for Anglers

## Overview
PlevenFishing is a specialized web platform designed for the angling community in the Pleven region, Bulgaria.
It provides a curated database of fishing locations, categorized by water body type and fishing methods,
integrated with Google Maps for precise navigation.

## Key Features
- Dynamic Content Management: Fully managed via Django Admin.
- Relational Data Structure: Link fishing reports (Posts) to specific locations using Django `ForeignKey`.
- Filtering: Custom-built logic to filter locations by methods (Feeder, Spinning, etc.) using `ManyToMany` relationships.
- Geospatial Integration: Embedded Google Maps API for precise location tracking.
- Frontend: Clean, semantic HTML and modular CSS architecture.
- SEO & UX Focused: Responsive design (Flexbox/Grid) with optimized typography (Google Fonts).

## Technical Stack
- Backend: Python , Django 
- Database: PostgreSQL (for Production) / SQL (for Development)
- Frontend: HTML, CSS, JavaScript
- Environment Management: Python-dotenv for secure credential handling.

## Installation & Setup
- ```bash
- git clone https://github.com/ivailoiliev89-netizen/Pleven-Fishing.git
- After installation, the user must log in to /admin and add objects with photos
- Create a .env file and populate it with your DB credentials (see settings.py for required keys).
- pip install -r requirements.txt
- python manage.py migrate
- python manage.py runserver

## Future Improvements
- Integration with a Weather API for real-time fishing conditions.
- Interactive "Catch Map" using Leaflet.js.