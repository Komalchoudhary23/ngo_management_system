# NGO Management System — Django

A full-stack **NGO Management System** developed using **Django (Python)** for managing NGO operations, donations, volunteers, events, staff, and website content through a dynamic admin dashboard. The system is designed to streamline NGO management by providing an easy-to-use platform for handling website content, enquiries, volunteers, donations, and staff administration.

---

## Table of Contents

- [Tech Stack](#tech-stack)
- [Features](#features)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Configuration](#configuration)
- [URL Reference](#url-reference)
- [Production Deployment](#production-deployment)
- [Security Roadmap](#security-roadmap)

---

## Tech Stack

| Layer      | Technology                        |
|------------|-----------------------------------|
| Backend    | Python 3.x, Django 4.x            |
| Database   | MySQL (compatible with existing schema) |
| Frontend   | HTML5, CSS3, JavaScript           |
| Server     | Gunicorn + Nginx (production)     |
| Sessions   | Django session framework          |
| File Storage | Local filesystem (`assets/uploads/`) |

---

## Features

**Public Website**
- Home page with dynamic banners
- About, Events, Donations, and Volunteer pages
- Contact form with enquiry management

**Admin Panel**
- Role-based access control (staff roles & permissions)
- CRUD operations for banners, events, donations, testimonials, volunteers, and staff
- CMS editor for About page content and site-wide settings
- Contact and donation enquiry inbox
- Image upload handling

---

## Project Structure

```
ngo/
├── manage.py
├── requirements.txt
│
├── ngo_project/                  # Django project configuration
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── ngo_app/                      # Main application
│   ├── models.py                 # All database models
│   ├── views_admin.py            # Admin panel views
│   ├── views_web.py              # Public website views
│   ├── urls.py                   # URL routing
│   ├── context_processors.py     # Injects site settings globally
│   ├── migrations/
│   └── templates/
│       ├── admin/                # Admin panel templates
│       │   ├── base.html
│       │   ├── login.html
│       │   ├── dashboard.html
│       │   └── ...
│       └── web/                  # Public website templates
│           ├── base.html
│           ├── home.html
│           ├── contact.html
│           └── ...
│
├── assets/                       # Static assets (CSS, JS, images)
│   ├── admin/
│   ├── web/
│   └── uploads/                  # User-uploaded media
│
├── media/                        # Runtime uploaded files
└── staticfiles/                  # Collected static files (production)
```

---

## Getting Started

### Prerequisites

- Python 3.8+
- MySQL Server
- pip

### Installation

**1. Clone the repository**
```bash
git clone <repository-url>
cd ngo
```

**2. Create and activate a virtual environment**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Copy the assets folder**

Place your `assets/` folder (containing `admin/`, `web/`, and `uploads/`) into the project root:
```
ngo/
│── manage.py
│── requirements.txt
│
├── ngo_project/                     # Django project configuration
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── ngo_app/                         # Main Django application
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── context_processors.py
│   ├── models.py
│   ├── urls.py
│   ├── views_admin.py
│   ├── views_web.py
│   ├── migrations/
│   │
│   └── templates/
│       ├── admin/
│       │   ├── base.html
│       │   ├── login.html
│       │   ├── dashboard.html
│       │   ├── list_banner.html
│       │   ├── add_banner.html
│       │   └── ...
│       │
│       └── web/
│           ├── base.html
│           ├── home.html
│           ├── about.html
│           ├── contact.html
│           ├── events.html
│           ├── donation.html
│           └── ...
│
├── assets/                          # Static assets
│   ├── admin/
│   ├── web/
│   └── uploads/
│```

**5. Configure the database** — see [Configuration](#configuration)

**6. Run migrations**
```bash
python manage.py migrate --run-syncdb
```
> This only creates Django's internal tables (sessions, etc.) and does not alter existing NGO tables.

**7. Start the development server**
```bash
python manage.py runserver
```

Visit: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## Configuration

Open `ngo_project/settings.py` and update the database block:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_mysql_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

> The Django models use `db_table` to match your existing MySQL table names exactly — no data re-import required.

---

## URL Reference

### Public Website

| URL          | Description          |
|--------------|----------------------|
| `/`          | Home page            |
| `/about`     | About Us             |
| `/events`    | Events listing       |
| `/donation`  | Donations listing    |
| `/volunteer` | Volunteers page      |
| `/contact`   | Contact form         |

### Admin Panel

| URL                  | Description                    |
|----------------------|--------------------------------|
| `/admin-login`       | Admin login                    |
| `/dashboard`         | Admin dashboard                |
| `/banner/list`       | Manage banners                 |
| `/donation/list`     | Manage donations               |
| `/events/list`       | Manage events                  |
| `/testimonial/list`  | Manage testimonials            |
| `/volunteer/list`    | Manage volunteers              |
| `/staff/list`        | Manage staff                   |
| `/role/list`         | Manage roles & permissions     |
| `/enquiry/contact`   | View contact enquiries         |
| `/enquiry/donation`  | View donation enquiries        |
| `/cms/about`         | Edit About page content        |
| `/cms/settings`      | Edit site-wide settings        |

---

## Production Deployment

**1. Update settings**
```python
DEBUG = False
ALLOWED_HOSTS = ['your-domain.com']
SECRET_KEY = 'your-secure-secret-key'
```

**2. Collect static files**
```bash
python manage.py collectstatic
```

**3. Run with Gunicorn**
```bash
pip install gunicorn
gunicorn ngo_project.wsgi:application --bind 0.0.0.0:8000
```

**4. Point Nginx to Gunicorn** and serve `staticfiles/` and `assets/uploads/` directly.

---

## Security Roadmap

The following improvements are recommended before production use:

- **Password hashing** — Passwords are currently stored as plain text to match the original PHP app. Replace the login check with Django's `check_password()` after hashing existing passwords:
  ```python
  from django.contrib.auth.hashers import check_password
  # Replace: password=password
  # With:    check_password(password, staff.password)
  ```
- **CSRF protection** — Ensure all POST forms include `{% csrf_token %}`.
- **Environment variables** — Move `SECRET_KEY`, database credentials, and `DEBUG` to a `.env` file (use `python-decouple` or `django-environ`).
- **HTTPS** — Configure SSL certificates in Nginx for production.

---

## License

This project is proprietary. All rights reserved.