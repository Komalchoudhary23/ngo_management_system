from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from ngo_app import views_web, views_admin   # ← FIXED: import from ngo_app, not from '.'

urlpatterns = [

    # =========================================================================
    # Website / Public Pages
    # =========================================================================
    path('', views_web.home, name='home'),
    path('about-us/', views_web.about_us, name='about_us'),
    path('events/', views_web.events, name='web_events'),
    path('event/<int:event_id>/', views_web.event_details, name='event_details_id'),
    path('donation/', views_web.donation, name='web_donation'),
    path('donation/<int:donation_id>/', views_web.donation_details, name='donation_details_id'),
    path('volunteer/', views_web.volunteer, name='web_volunteer'),
    path('contact/', views_web.contact, name='contact'),
    path('projects/', views_web.projects, name='projects'),

    # Public AJAX endpoints
    path('insert-contact-enquiry/', views_web.insert_contact_enquiry_data, name='insert_contact_enquiry_data'),
    path('insert-donation-enquiry/', views_web.insert_donation_enquiry_data, name='insert_donation_enquiry'),

    # =========================================================================
    # Admin Auth
    # =========================================================================
    path('admin-login/', views_admin.admin_login, name='admin_login'),
    path('admin-logout/', views_admin.admin_logout, name='admin_logout'),

    # =========================================================================
    # Dashboard
    # =========================================================================
    path('dashboard/', views_admin.dashboard, name='dashboard'),

    # =========================================================================
    # Banner
    # =========================================================================
    path('banner/', views_admin.list_banner, name='list_banner'),
    path('banner/add/', views_admin.add_banner, name='add_banner'),
    path('banner/edit/<int:banner_id>/', views_admin.edit_banner, name='edit_banner'),
    path('banner/insert/', views_admin.insert_banner_data, name='insert_banner_data'),
    path('banner/delete/', views_admin.delete_banner, name='delete_banner'),

    # =========================================================================
    # Donation
    # =========================================================================
    path('donation-list/', views_admin.list_donation, name='list_donation'),
    path('donation/add/', views_admin.add_donation, name='add_donation'),
    path('donation/edit/<int:donation_id>/', views_admin.edit_donation, name='edit_donation'),
    path('donation/insert/', views_admin.insert_donation_data, name='insert_donation_data'),
    path('donation/delete/', views_admin.delete_donation, name='delete_donation'),
    path('donation/update-status/', views_admin.update_donation_status, name='update_donation_status'),

    # =========================================================================
    # Events
    # =========================================================================
    path('events-list/', views_admin.list_events, name='list_events'),
    path('events/add/', views_admin.add_events, name='add_events'),
    path('events/edit/<int:events_id>/', views_admin.edit_events, name='edit_events'),
    path('events/insert/', views_admin.insert_events_data, name='insert_events_data'),
    path('events/delete/', views_admin.delete_events, name='delete_events'),
    path('events/update-status/', views_admin.update_events_status, name='update_events_status'),

    # =========================================================================
    # Testimonial
    # =========================================================================
    path('testimonial/', views_admin.list_testimonial, name='list_testimonial'),
    path('testimonial/add/', views_admin.add_testimonial, name='add_testimonial'),
    path('testimonial/edit/<int:testimonial_id>/', views_admin.edit_testimonial, name='edit_testimonial'),
    path('testimonial/insert/', views_admin.insert_testimonial_data, name='insert_testimonial_data'),
    path('testimonial/delete/', views_admin.delete_testimonial, name='delete_testimonial'),
    path('testimonial/update-status/', views_admin.update_testimonial_status, name='update_testimonial_status'),

    # =========================================================================
    # Volunteer
    # =========================================================================
    path('volunteer-list/', views_admin.list_volunteer, name='list_volunteer'),
    path('volunteer/add/', views_admin.add_volunteer, name='add_volunteer'),
    path('volunteer/edit/<int:volunteer_id>/', views_admin.edit_volunteer, name='edit_volunteer'),
    path('volunteer/insert/', views_admin.insert_volunteer_data, name='insert_volunteer_data'),
    path('volunteer/delete/', views_admin.delete_volunteer, name='delete_volunteer'),

    # =========================================================================
    # Staff
    # =========================================================================
    path('staff/', views_admin.list_staff, name='list_staff'),
    path('staff/add/', views_admin.add_staff, name='add_staff'),
    path('staff/edit/<int:staff_id>/', views_admin.edit_staff, name='edit_staff'),
    path('staff/insert/', views_admin.insert_staff_data, name='insert_staff_data'),
    path('staff/delete/', views_admin.delete_staff, name='delete_staff'),
    path('staff/update-status/', views_admin.update_staff_status, name='update_staff_status'),

    # =========================================================================
    # Role & Permissions
    # =========================================================================
    path('role/', views_admin.list_role, name='list_role'),
    path('role/add/', views_admin.add_role, name='add_role'),
    path('role/edit/<int:role_id>/', views_admin.edit_role, name='edit_role'),
    path('role/insert/', views_admin.insert_permission, name='insert_permission'),
    path('role/delete/', views_admin.delete_role, name='delete_role'),
    path('role/update-status/', views_admin.update_role_status, name='update_role_status'),

    # =========================================================================
    # Enquiries
    # =========================================================================
    path('contact-enquiry/', views_admin.contact_enquiry, name='contact_enquiry'),
    path('contact-enquiry/delete/', views_admin.delete_contact_enquiry, name='delete_contact_enquiry'),
    path('donation-enquiry/', views_admin.donation_enquiry, name='donation_enquiry'),
    path('donation-enquiry/delete/', views_admin.delete_donation_enquiry, name='delete_donation_enquiry'),

    # =========================================================================
    # CMS
    # =========================================================================
    path('cms/about/', views_admin.about_page, name='about_page'),
    path('cms/about/insert/', views_admin.insert_about_page_data, name='insert_about_page_data'),
    path('cms/settings/', views_admin.setting_page, name='setting_page'),
    path('cms/settings/insert/', views_admin.insert_setting_page_data, name='insert_setting_page_data'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
