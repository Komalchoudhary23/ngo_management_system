# NGO Management System — Django

A full-stack **NGO Management System** developed using **Django (Python)** for managing NGO operations, donations, volunteers, events, staff, and website content through a dynamic admin dashboard. The system is designed to streamline NGO management by providing an easy-to-use platform for handling website content, enquiries, volunteers, donations, and staff administration.

---

## Table of Contents

- [Tech Stack](#tech-stack)
- [Features](#features)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)

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


## License

This project is proprietary. All rights reserved.
