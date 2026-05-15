from django.urls import path
from . import views_web, views_admin

urlpatterns = [

    # Website Pages
    path('', views_web.home, name='home'),
    path('about-us/', views_web.about_us, name='about_us'),
    path('events/', views_web.events, name='web_events'),
    path('event/<int:event_id>/', views_web.event_details, name='event_details_id'),

    path('donation/', views_web.donation, name='web_donation'),
    path('donation/<int:donation_id>/', views_web.donation_details, name='donation_details_id'),

    path('volunteer/', views_web.volunteer, name='web_volunteer'),
    path('contact/', views_web.contact, name='contact'),

    # Admin Panel
    path('admin-login/', views_admin.admin_login, name='admin_login'),
    path('dashboard/', views_admin.dashboard, name='dashboard'),

    # Banner
    path('banner/', views_admin.list_banner, name='list_banner'),
    path('banner/add/', views_admin.add_banner, name='add_banner'),

    # Donation
    path('donation-list/', views_admin.list_donation, name='list_donation'),
    path('donation/add/', views_admin.add_donation, name='add_donation'),

    # Events
    path('events-list/', views_admin.list_events, name='list_events'),
    path('events/add/', views_admin.add_events, name='add_events'),
]