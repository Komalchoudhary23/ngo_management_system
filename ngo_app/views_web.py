import os
import time
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.conf import settings

from .models import (
    Banner, Donation, Events, Testimonial, Volunteer,
    ContactEnquiry, DonationEnquiry
)


# ─── Public Web Pages ────────────────────────────────────────────────────────

def home(request):
    context = {
        'testimonial_data': Testimonial.objects.all(),
        'banner_data': Banner.objects.all(),
        'donation_data': Donation.objects.all(),
        'events_data': Events.objects.all(),
    }
    return render(request, 'web/home.html', context)


def about_us(request):
    from .models import CmsAbout
    about_data = CmsAbout.objects.first()
    return render(request, 'web/about.html', {
        'title': 'Saverahamara | About Us',
        'about_data': about_data,
    })


def events(request):
    event_data = Events.objects.filter(status='1')
    return render(request, 'web/events.html', {
        'title': 'Saverahamara | Events',
        'event_data': event_data,
    })


def event_details(request, event_id=None):
    event = None
    if event_id:
        try:
            event = Events.objects.get(id=event_id, status='1')
        except Events.DoesNotExist:
            pass
    return render(request, 'web/event-details.html', {
        'title': 'Saverahamara | Event Details',
        'event': event,
    })


def donation(request):
    donation_data = Donation.objects.filter(status='1')
    return render(request, 'web/donation.html', {
        'title': 'Saverahamara | Donation',
        'donation_data': donation_data,
    })


def donation_details(request, donation_id=None):
    don = None
    if donation_id:
        try:
            don = Donation.objects.get(id=donation_id, status='1')
        except Donation.DoesNotExist:
            pass
    return render(request, 'web/donation-details.html', {
        'title': 'Saverahamara | Donation Details',
        'donation': don,
    })


def volunteer(request):
    volunteer_data = Volunteer.objects.filter(status='1')
    return render(request, 'web/volunteer.html', {
        'title': 'Saverahamara | Volunteer',
        'volunteer_data': volunteer_data,
    })


def contact(request):
    return render(request, 'web/contact.html', {'title': 'Saverahamara | Contact'})


# ─── Public AJAX Endpoints ───────────────────────────────────────────────────

@require_POST
def insert_contact_enquiry_data(request):
    data = {
        'name': request.POST.get('name', ''),
        'email': request.POST.get('email', ''),
        'phone': request.POST.get('phone', ''),
        'message': request.POST.get('message', ''),
    }
    try:
        ContactEnquiry.objects.create(**data)
        return JsonResponse({'status': True, 'msg': 'Thank you for Choosing Us. Our Team will soon contact you.'})
    except Exception as e:
        return JsonResponse({'status': False, 'msg': str(e)})


@require_POST
def insert_donation_enquiry_data(request):
    image_path = ''
    uploaded_file = request.FILES.get('image')
    if uploaded_file:
        upload_dir = os.path.join(settings.MEDIA_ROOT, 'donation_images')
        os.makedirs(upload_dir, exist_ok=True)
        ext = os.path.splitext(uploaded_file.name)[1]
        filename = f"{int(time.time())}_{uploaded_file.name}"
        dest = os.path.join(upload_dir, filename)
        with open(dest, 'wb+') as f:
            for chunk in uploaded_file.chunks():
                f.write(chunk)
        image_path = f"assets/uploads/donation_images/{filename}"

    data = {
        'name': request.POST.get('name', ''),
        'phone': request.POST.get('phone', ''),
        'email': request.POST.get('email', ''),
        'image': image_path,
    }
    try:
        DonationEnquiry.objects.create(**data)
        return JsonResponse({'status': True, 'msg': 'Thank you for Choosing Us. Our Team will soon contact you.'})
    except Exception as e:
        return JsonResponse({'status': False, 'msg': str(e)})


def projects(request):
    from .models import Donation
    donation_data = Donation.objects.filter(status='1')
    return render(request, 'web/projects.html', {
        'title': 'Saverahamara | Projects',
        'donation_data': donation_data,
    })
