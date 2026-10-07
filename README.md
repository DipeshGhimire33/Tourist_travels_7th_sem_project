# Tourist Travels – Nepal Tourism & Booking Platform

A Django web application for planning and booking trips in Nepal. Travelers can explore destinations, find and book hotels, hire guides and vehicles, rent trekking gear, and plan routes on an interactive map, all in one place.

> BSc.CSIT final year project (7th semester).

---

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Configuration](#configuration)
- [User Roles](#user-roles)
- [Data Model Overview](#data-model-overview)
- [Main Routes](#main-routes)
- [Security Notes](#security-notes)
- [Future Improvements](#future-improvements)
- [Author](#author)

---

## Features

**For travelers (customers)**
- Browse destinations with descriptions, popular places and must-visit spots
- Search and filter hotels, view details, and book rooms by date range
- Add a guide and a vehicle to a hotel booking
- Rent equipment (camera, camping, clothing, hiking gear) through a cart
- Build custom travel packages (vehicle + equipment + days) with calculated pricing
- Plan trips on an interactive map with pickup/destination coordinates and route display
- Pay for bookings, view booking confirmation, and cancel bookings
- Rate and review hotels and the app, and share destination experiences in a photo gallery
- Contact form and customer profile management

**For hotel owners**
- Register and manage hotels (create, edit, delete)
- Manage rooms, pricing and availability
- Dedicated owner dashboard and profile

**For admins**
- Dashboard and Django admin for managing destinations, guides, vehicles, equipment and users

**Maps module**
- Tourist attractions and EV charging stations stored as map locations
- Location search by name or address, plus built-in city centers (Kathmandu, Pokhara, Chitwan, Lumbini, Bhaktapur, Patan)
- Nearby attraction/EV station lookup using the Haversine distance
- Road routing with alternative routes via the OSRM public API, with a straight-line fallback if routing fails
- Detects attractions and EV charging stations within 10 km of each route

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | Python, Django 5.2 |
| Database | SQLite (default) |
| Frontend | Django templates, HTML, CSS, JavaScript |
| Maps / Routing | OSRM public routing API |
| Image handling | Pillow |
| Config | python-dotenv |
| HTTP client | requests |

---

## Project Structure

```
Tourist_travels_7th_sem_project/
├── finalYearProject/   # Django project settings, root URLs, WSGI/ASGI
├── reserve/            # Core app: hotels, bookings, guides, equipment, packages, reviews
├── maps/               # Maps app: attractions, EV stations, routing APIs
├── templates/          # HTML templates
├── static/             # CSS, JS, images
├── media/              # User-uploaded files (images)
├── manage.py
├── requirements.txt
├── .env                # Environment variables (do not commit real secrets)
└── db.sqlite3          # Development database
```

---

## Getting Started

### Prerequisites
- Python 3.10 or newer
- pip
- Git

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/DipeshGhimire33/Tourist_travels_7th_sem_project.git
cd Tourist_travels_7th_sem_project

# 2. Create and activate a virtual environment
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply database migrations
python manage.py migrate

# 5. Create an admin account
python manage.py createsuperuser

# 6. Run the development server
python manage.py runserver
```

Open <http://127.0.0.1:8000/> in your browser. The admin panel is at `/admin/`.

> The repository ships with a sample `db.sqlite3`. If you prefer a clean start, delete it before running `migrate`.

---

## Configuration

Create a `.env` file in the project root for any secrets or environment-specific values:

```env
SECRET_KEY=your-secret-key
DEBUG=True
```

Email (for password reset) is configured in `finalYearProject/settings.py`. To enable it, set the SMTP settings and load credentials from environment variables rather than hard-coding them:

```python
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
```

Uploaded images are stored under `media/` (`MEDIA_URL = /media/`).

---

## User Roles

| Role | Capabilities |
|------|--------------|
| **Customer** | Browse, search, book hotels, rent equipment, create packages, review, upload experiences |
| **Hotel Owner** | Register and manage own hotels and rooms, view owner dashboard |
| **Admin** | Full access through the dashboard and Django admin |

---

## Data Model Overview

Key models in `reserve/models.py`:

- **Destination**, **DestinationPopular**, **DestinationMustVisit**: places to explore
- **Hotel**, **Room**: accommodation and room inventory
- **Guide**, **Vehicle**, **Equipment**: bookable services and rentals
- **Trip**, **Booking**, **BookingEquipment**, **HotelBooking**, **Package**: trip planning, reservations and pricing
- **HotelReview**, **AppReview**, **DestinationExperience**, **ContactMessage**: feedback and community content
- **Customer**, **HotelOwner**, **UserProfile**: user profiles and roles

Key models in `maps/`: **TouristAttraction**, **EVChargingStation**, **Route**, **Waypoint**.

---

## Main Routes

| Path | Description |
|------|-------------|
| `/reserve/` | Home page |
| `/reserve/hotels/` | Hotel listing |
| `/reserve/search/` | Hotel search |
| `/reserve/hotel/book/<id>/` | Book a room |
| `/reserve/destinations/<id>/` | Destination details |
| `/reserve/equipment/` | Equipment rental and cart |
| `/reserve/packages/` | Travel packages |
| `/reserve/create-package/` | Build a custom package |
| `/reserve/payment/` | Payment |
| `/reserve/maps/` | Interactive trip map |
| `/reserve/gallery/` | Experience gallery |
| `/reserve/contact_us/` | Contact form |
| `/admin/` | Django admin |

Maps API endpoints (served by the `maps` app) include location search, nearby lookup, all locations, and route calculation.

---

## Security Notes

This project is configured for **local development only**. Before any deployment:

- Move `SECRET_KEY` out of source control and set `DEBUG = False`
- Set `ALLOWED_HOSTS` appropriately
- Never commit `.env`, real credentials, or the `.venv` folder (add them to `.gitignore`)
- Rotate any credentials that were ever committed to the repository
- Review `@csrf_exempt` endpoints (e.g. route calculation) and add proper protection
- Replace SQLite with a production database such as PostgreSQL

---

## Future Improvements

- Online payment gateway integration (eSewa / Khalti)
- Email confirmations and booking notifications
- REST API and mobile app
- Multi-language support (English / Nepali)
- Automated tests and CI

---

## Author

Lead Developer : **Dipesh Ghimire**
Developer : **Bhijan Bastola**
QA : **Jharna Poudel**

GitHub: [@DipeshGhimire33](https://github.com/DipeshGhimire33)
