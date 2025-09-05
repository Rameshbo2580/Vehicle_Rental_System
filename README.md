# Vehicle_Rental_System

A Django-based web application for managing vehicle rentals, including cars, bikes, and scooters. Users can browse available vehicles, book them, and manage rentals easily.

---

## Features

- Add, update, and delete vehicles (Cars, Bikes, Scooters)
- Upload vehicle images
- User-friendly booking system
- Manage vehicle availability
- Responsive design for web browsers

---

## Requirements

- Python 3.10+ (tested with Python 3.12)
- Django 5.2.6
- Pillow (for image handling)

---

## Installation

1. **Clone the repository**
```bash
git clone <repo-url>
cd Vehicle_Rental_System

2.**Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate   # Linux/Mac
# OR
venv\Scripts\activate      # Windows

3.**Install dependencies
pip install -r requirements.txt
# OR manually
pip install django pillow

4.**Apply migrations
python3 manage.py makemigrations
python3 manage.py migrate

5.**Run the development server
python3 manage.py runserver
