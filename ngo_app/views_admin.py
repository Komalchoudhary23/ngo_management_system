import os
import time
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.conf import settings
from django.utils import timezone

from .models import (
    Banner, Donation, Events, Role, Permission, PermissionType,
    Staff, Testimonial, Volunteer, ContactEnquiry, DonationEnquiry,
    CmsAbout, CmsSetting
)


# ─── Helpers ────────────────────────────────────────────────────────────────

def login_required_json(view_func):
    """Decorator that returns JSON 403 for AJAX endpoints if not logged in."""
    def wrapper(request, *args, **kwargs):
        if not request.session.get('onepixel'):
            return JsonResponse({'status': False, 'msg': 'Unauthorized'}, status=403)
        return view_func(request, *args, **kwargs)
    return wrapper


def admin_login_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.session.get('onepixel'):
            return redirect('admin_login')
        return view_func(request, *args, **kwargs)
    return wrapper


def handle_upload(request, file_field, upload_subdir, existing_filename=''):
    """Save an uploaded file and return its filename, or return existing name."""
    upload_dir = os.path.join(settings.MEDIA_ROOT, upload_subdir)
    os.makedirs(upload_dir, exist_ok=True)

    uploaded_file = request.FILES.get(file_field)
    if not uploaded_file:
        return existing_filename

    # Delete old file if replacing
    if existing_filename:
        old_path = os.path.join(upload_dir, existing_filename)
        if os.path.exists(old_path):
            os.remove(old_path)

    ext = os.path.splitext(uploaded_file.name)[1]
    filename = f"{int(time.time())}{ext}"
    dest = os.path.join(upload_dir, filename)
    with open(dest, 'wb+') as f:
        for chunk in uploaded_file.chunks():
            f.write(chunk)
    return filename


# ─── Auth ───────────────────────────────────────────────────────────────────

def admin_login(request):
    # Already logged in → go to dashboard
    if request.session.get('onepixel'):
        return redirect('dashboard')

    error = None

    if request.method == 'POST':
        username = request.POST.get('user_id', '').strip()
        password = request.POST.get('password', '').strip()

        # FIX 1: Debug print to server console so you can see what is being matched
        # Remove these prints once login works
        print(f"[LOGIN ATTEMPT] email='{username}' password='{password}'")

        try:
            # FIX 2: Match on email + plain-text password + active status
            # Make sure the Staff row in MySQL has status='1' and password stored as plain text
            staff = Staff.objects.get(email_id=username, password=password, status='1')

            print(f"[LOGIN SUCCESS] staff.name='{staff.name}' staff.user_id='{staff.user_id}'")

            # Build permission map
            view_menu = {}
            try:
                role = Role.objects.get(id=staff.role_id)
                perm_ids = [int(x) for x in role.permission_ids.split(',') if x.strip()]
                permissions = Permission.objects.filter(id__in=perm_ids)
                for perm in permissions:
                    try:
                        ptype = PermissionType.objects.get(id=perm.permission_type_id)
                        key = ptype.view_name.replace(' ', '_')
                        view_menu.setdefault(key, []).append(perm.name)
                    except PermissionType.DoesNotExist:
                        pass
            except Role.DoesNotExist:
                pass

            # FIX 3: Set session and explicitly mark as modified so Django saves it
            request.session['onepixel'] = {
                'user': staff.name,
                'user_id': str(staff.user_id),   # ensure it's JSON-serializable
                'photo': staff.photo or '',
                'access_level': str(staff.access_level) if staff.access_level else '',
                'address': staff.address or '',
                'role_id': str(staff.role_id) if staff.role_id else '',
                'permission': view_menu,
            }
            request.session.modified = True   # ← FIX: force Django to save session

            return redirect('dashboard')

        except Staff.DoesNotExist:
            print(f"[LOGIN FAILED] No staff found for email='{username}'")
            # FIX 4: Use error variable instead of broken redirect with query string
            error = 'Invalid email or password. Please try again.'

    return render(request, 'admin/login.html', {'error': error})


def admin_logout(request):
    request.session.flush()
    return redirect('admin_login')


# ─── Dashboard ──────────────────────────────────────────────────────────────

@admin_login_required
def dashboard(request):
    context = {
        'total_blogs': 0,
        'total_staff': Staff.objects.count(),
        'total_banner': Banner.objects.count(),
        'total_donation': Donation.objects.count(),
        'total_events': Events.objects.count(),
        'total_volunteer': Volunteer.objects.count(),
        'total_contact': ContactEnquiry.objects.count(),
        'total_testimonial': Testimonial.objects.count(),
        'total_donation_enquiry': DonationEnquiry.objects.count(),
    }
    return render(request, 'admin/dashboard.html', context)


# ─── Banner ─────────────────────────────────────────────────────────────────

@admin_login_required
def list_banner(request):
    banners = Banner.objects.all()
    return render(request, 'admin/list_banner.html', {'banner_data': banners})


@admin_login_required
def add_banner(request):
    return render(request, 'admin/add_banner.html', {'form_type': 'Add'})


@admin_login_required
def edit_banner(request, banner_id):
    banner = get_object_or_404(Banner, id=banner_id)
    return render(request, 'admin/add_banner.html', {'form_type': 'Edit', 'banner_data': [banner]})


@admin_login_required
@require_POST
def insert_banner_data(request):
    form_type = request.POST.get('form_type')
    existing = request.POST.get('banner_recent_photo', '')
    img = handle_upload(request, 'banner_photo', 'banner', existing)

    data = {
        'banner_name': request.POST.get('banner_name', ''),
        'banner_img': img,
        'status': '1',
    }
    try:
        if form_type == 'Add':
            Banner.objects.create(**data)
        else:
            Banner.objects.filter(id=request.POST.get('banner_id')).update(**data)
        return JsonResponse({'status': True, 'msg': 'Data Saved'})
    except Exception as e:
        return JsonResponse({'status': False, 'msg': str(e)})


@admin_login_required
@require_POST
def delete_banner(request):
    banner_id = request.POST.get('banner_id')
    deleted, _ = Banner.objects.filter(id=banner_id).delete()
    return JsonResponse({'result': 'true' if deleted else 'false'}, safe=False)


# ─── Donation ───────────────────────────────────────────────────────────────

@admin_login_required
def list_donation(request):
    donations = Donation.objects.all()
    return render(request, 'admin/list_donation.html', {'donation_data': donations})


@admin_login_required
def add_donation(request):
    return render(request, 'admin/add_donation.html', {'form_type': 'Add'})


@admin_login_required
def edit_donation(request, donation_id):
    donation = get_object_or_404(Donation, id=donation_id)
    return render(request, 'admin/add_donation.html', {'form_type': 'Edit', 'donation_data': [donation]})


@admin_login_required
@require_POST
def insert_donation_data(request):
    form_type = request.POST.get('form_type')
    existing = request.POST.get('donation_recent_photo', '')
    img = handle_upload(request, 'donation_photo', 'donation', existing)

    data = {
        'donation_name': request.POST.get('donation_name', ''),
        'description': request.POST.get('description', ''),
        'donation_img': img,
        'status': '1',
    }
    try:
        if form_type == 'Add':
            Donation.objects.create(**data)
        else:
            Donation.objects.filter(id=request.POST.get('donation_id')).update(**data)
        return JsonResponse({'status': True, 'msg': 'Data Saved'})
    except Exception as e:
        return JsonResponse({'status': False, 'msg': str(e)})


@admin_login_required
@require_POST
def delete_donation(request):
    donation_id = request.POST.get('donation_id')
    deleted, _ = Donation.objects.filter(id=donation_id).delete()
    return JsonResponse({'result': 'true' if deleted else 'false'}, safe=False)


@admin_login_required
@require_POST
def update_donation_status(request):
    donation_id = request.POST.get('donation_id')
    try:
        obj = Donation.objects.get(id=donation_id)
        obj.status = '0' if obj.status == '1' else '1'
        obj.save()
        return JsonResponse({'result': 'true'}, safe=False)
    except Donation.DoesNotExist:
        return JsonResponse({'result': 'false'}, safe=False)


# ─── Events ─────────────────────────────────────────────────────────────────

@admin_login_required
def list_events(request):
    events = Events.objects.order_by('-id')
    return render(request, 'admin/list_events.html', {'events_data': events})


@admin_login_required
def add_events(request):
    return render(request, 'admin/add_events.html', {'form_type': 'Add'})


@admin_login_required
def edit_events(request, events_id):
    event = get_object_or_404(Events, id=events_id)
    return render(request, 'admin/add_events.html', {'form_type': 'Edit', 'events_data': [event]})


@admin_login_required
@require_POST
def insert_events_data(request):
    form_type = request.POST.get('form_type')
    banner_existing = request.POST.get('events_banner_recent_photo', '')
    img_existing = request.POST.get('events_recent_photo', '')

    banner_img = handle_upload(request, 'events_banner_photo', 'events', banner_existing)
    events_img = handle_upload(request, 'events_photo', 'events', img_existing)

    data = {
        'events_name': request.POST.get('events_name', ''),
        'about_events': request.POST.get('about_events', ''),
        'events_content': request.POST.get('events_content', ''),
        'status': '1',
    }
    if banner_img:
        data['events_banner_img'] = banner_img
    if events_img:
        data['events_img'] = events_img

    try:
        if form_type == 'Add':
            Events.objects.create(**data)
        else:
            Events.objects.filter(id=request.POST.get('events_id')).update(**data)
        return JsonResponse({'status': True, 'msg': 'Data Saved'})
    except Exception as e:
        return JsonResponse({'status': False, 'msg': str(e)})


@admin_login_required
@require_POST
def delete_events(request):
    events_id = request.POST.get('events_id')
    deleted, _ = Events.objects.filter(id=events_id).delete()
    return JsonResponse({'result': 'true' if deleted else 'false'}, safe=False)


@admin_login_required
@require_POST
def update_events_status(request):
    events_id = request.POST.get('events_id')
    try:
        obj = Events.objects.get(id=events_id)
        obj.status = '0' if obj.status == '1' else '1'
        obj.save()
        return JsonResponse({'result': 'true'}, safe=False)
    except Events.DoesNotExist:
        return JsonResponse({'result': 'false'}, safe=False)


# ─── Testimonial ────────────────────────────────────────────────────────────

@admin_login_required
def list_testimonial(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'admin/list_testimonial.html', {'testimonial_data': testimonials})


@admin_login_required
def add_testimonial(request):
    return render(request, 'admin/add_testimonial.html', {'form_type': 'Add'})


@admin_login_required
def edit_testimonial(request, testimonial_id):
    t = get_object_or_404(Testimonial, id=testimonial_id)
    return render(request, 'admin/add_testimonial.html', {'form_type': 'Edit', 'testimonial_data': [t]})


@admin_login_required
@require_POST
def insert_testimonial_data(request):
    form_type = request.POST.get('form_type')
    existing = request.POST.get('testimonial_recent_photo', '')
    img = handle_upload(request, 'testimonial_photo', 'testimonial', existing)

    data = {
        'testimonial_name': request.POST.get('testimonial_name', ''),
        'description': request.POST.get('description', ''),
        'occupation': request.POST.get('occupation', ''),
        'testimonial_img': img,
        'status': '1',
    }
    try:
        if form_type == 'Add':
            Testimonial.objects.create(**data)
        else:
            Testimonial.objects.filter(id=request.POST.get('testimonial_id')).update(**data)
        return JsonResponse({'status': True, 'msg': 'Data Saved'})
    except Exception as e:
        return JsonResponse({'status': False, 'msg': str(e)})


@admin_login_required
@require_POST
def delete_testimonial(request):
    t_id = request.POST.get('testimonial_id')
    deleted, _ = Testimonial.objects.filter(id=t_id).delete()
    return JsonResponse({'result': 'true' if deleted else 'false'}, safe=False)


@admin_login_required
@require_POST
def update_testimonial_status(request):
    t_id = request.POST.get('testimonial_id')
    try:
        obj = Testimonial.objects.get(id=t_id)
        obj.status = '0' if obj.status == '1' else '1'
        obj.save()
        return JsonResponse({'result': 'true'}, safe=False)
    except Testimonial.DoesNotExist:
        return JsonResponse({'result': 'false'}, safe=False)


# ─── Volunteer ──────────────────────────────────────────────────────────────

@admin_login_required
def list_volunteer(request):
    volunteers = Volunteer.objects.all()
    return render(request, 'admin/list_volunteer.html', {'volunteer_data': volunteers})


@admin_login_required
def add_volunteer(request):
    return render(request, 'admin/add_volunteer.html', {'form_type': 'Add'})


@admin_login_required
def edit_volunteer(request, volunteer_id):
    v = get_object_or_404(Volunteer, id=volunteer_id)
    return render(request, 'admin/add_volunteer.html', {'form_type': 'Edit', 'volunteer_data': [v]})


@admin_login_required
@require_POST
def insert_volunteer_data(request):
    form_type = request.POST.get('form_type')
    existing = request.POST.get('volunteer_recent_photo', '')
    img = handle_upload(request, 'volunteer_photo', 'volunteer', existing)

    data = {
        'volunteer_name': request.POST.get('volunteer_name', ''),
        'volunteer_img': img,
        'status': '1',
    }
    try:
        if form_type == 'Add':
            Volunteer.objects.create(**data)
        else:
            Volunteer.objects.filter(id=request.POST.get('volunteer_id')).update(**data)
        return JsonResponse({'status': True, 'msg': 'Data Saved'})
    except Exception as e:
        return JsonResponse({'status': False, 'msg': str(e)})


@admin_login_required
@require_POST
def delete_volunteer(request):
    v_id = request.POST.get('volunteer_id')
    deleted, _ = Volunteer.objects.filter(id=v_id).delete()
    return JsonResponse({'result': 'true' if deleted else 'false'}, safe=False)


# ─── Staff ──────────────────────────────────────────────────────────────────

@admin_login_required
def list_staff(request):
    staff_list = Staff.objects.all()
    roles = {r.id: r.name for r in Role.objects.all()}
    for s in staff_list:
        s.rolename = roles.get(s.role_id, '')
    return render(request, 'admin/list_staff.html', {'staff_data': staff_list})


@admin_login_required
def add_staff(request):
    roles = Role.objects.filter(status='1')
    return render(request, 'admin/add_staff.html', {'form_type': 'Add', 'role_data': roles})


@admin_login_required
def edit_staff(request, staff_id):
    staff = get_object_or_404(Staff, user_id=staff_id)
    roles = Role.objects.filter(status='1')
    return render(request, 'admin/add_staff.html', {
        'form_type': 'Edit', 'staff_data': [staff], 'role_data': roles
    })


@admin_login_required
@require_POST
def insert_staff_data(request):
    form_type = request.POST.get('form_type')
    existing = request.POST.get('staff_recent_photo', '')
    img = handle_upload(request, 'photo', 'users', existing)

    data = {
        'name': request.POST.get('name', ''),
        'photo': img,
        'role_id': request.POST.get('role_id'),
        'mobile_no': request.POST.get('mobile_no', ''),
        'email_id': request.POST.get('email_id', ''),
        'password': request.POST.get('password', ''),
        'address': request.POST.get('address', ''),
        'status': '1',
    }
    try:
        if form_type == 'Add':
            Staff.objects.create(**data)
        else:
            Staff.objects.filter(user_id=request.POST.get('staff_id')).update(**data)
        return JsonResponse({'status': True, 'msg': 'Data Saved'})
    except Exception as e:
        return JsonResponse({'status': False, 'msg': str(e)})


@admin_login_required
@require_POST
def delete_staff(request):
    staff_id = request.POST.get('staff_id')
    deleted, _ = Staff.objects.filter(user_id=staff_id).delete()
    return JsonResponse({'result': 'true' if deleted else 'false'}, safe=False)


@admin_login_required
@require_POST
def update_staff_status(request):
    staff_id = request.POST.get('staff_id')
    try:
        obj = Staff.objects.get(user_id=staff_id)
        obj.status = '0' if obj.status == '1' else '1'
        obj.save()
        return JsonResponse({'result': 'true'}, safe=False)
    except Staff.DoesNotExist:
        return JsonResponse({'result': 'false'}, safe=False)


# ─── Role ───────────────────────────────────────────────────────────────────

@admin_login_required
def list_role(request):
    roles = Role.objects.all()
    return render(request, 'admin/list_role.html', {'role_data': roles})


@admin_login_required
def add_role(request):
    permission_types = list(PermissionType.objects.filter(status='1'))
    for pt in permission_types:
        pt.permission_data = Permission.objects.filter(permission_type_id=pt.id, status='1')
    return render(request, 'admin/add_role.html', {
        'form_type': 'Add',
        'permission_type_data': permission_types,
        'access_data': [],
    })


@admin_login_required
def edit_role(request, role_id):
    role = get_object_or_404(Role, id=role_id)
    permission_types = list(PermissionType.objects.filter(status='1'))
    for pt in permission_types:
        pt.permission_data = Permission.objects.filter(permission_type_id=pt.id, status='1')
    access_data = [x.strip() for x in role.permission_ids.split(',') if x.strip()]
    return render(request, 'admin/add_role.html', {
        'form_type': 'Edit',
        'permission_type_data': permission_types,
        'role_data': [role],
        'access_data': access_data,
    })


@admin_login_required
@require_POST
def insert_permission(request):
    form_type = request.POST.get('form_type')
    permissions = request.POST.getlist('permissions')
    data = {
        'name': request.POST.get('role_name', ''),
        'permission_ids': ','.join(permissions),
        'entry_date_time': timezone.now(),
        'status': '1',
    }
    try:
        if form_type == 'Add':
            Role.objects.create(**data)
        else:
            Role.objects.filter(id=request.POST.get('role_id')).update(**data)
        return JsonResponse({'status': True, 'msg': 'Data Saved'})
    except Exception as e:
        return JsonResponse({'status': False, 'msg': str(e)})


@admin_login_required
@require_POST
def delete_role(request):
    role_id = request.POST.get('role_id')
    deleted, _ = Role.objects.filter(id=role_id).delete()
    return JsonResponse({'result': 'true' if deleted else 'false'}, safe=False)


@admin_login_required
@require_POST
def update_role_status(request):
    role_id = request.POST.get('role_id')
    try:
        obj = Role.objects.get(id=role_id)
        obj.status = '0' if obj.status == '1' else '1'
        obj.save()
        return JsonResponse({'result': 'true'}, safe=False)
    except Role.DoesNotExist:
        return JsonResponse({'result': 'false'}, safe=False)


# ─── Enquiry ────────────────────────────────────────────────────────────────

@admin_login_required
def contact_enquiry(request):
    enquiries = ContactEnquiry.objects.order_by('-id')
    return render(request, 'admin/contact_enquiry.html', {'contact_enquiry_data': enquiries})


@admin_login_required
@require_POST
def delete_contact_enquiry(request):
    eid = request.POST.get('contact_enquiry_id')
    deleted, _ = ContactEnquiry.objects.filter(id=eid).delete()
    return JsonResponse({'result': 'true' if deleted else 'false'}, safe=False)


@admin_login_required
def donation_enquiry(request):
    enquiries = DonationEnquiry.objects.order_by('-id')
    return render(request, 'admin/donation_enquiry.html', {'donation_data': enquiries})


@admin_login_required
@require_POST
def delete_donation_enquiry(request):
    eid = request.POST.get('donation_id')
    deleted, _ = DonationEnquiry.objects.filter(id=eid).delete()
    return JsonResponse({'result': 'true' if deleted else 'false'}, safe=False)


# ─── CMS - About Page ───────────────────────────────────────────────────────

@admin_login_required
def about_page(request):
    about_data = CmsAbout.objects.all()
    return render(request, 'admin/about_page.html', {'about_page_data': about_data})


@admin_login_required
@require_POST
def insert_about_page_data(request):
    data = {
        'heading': request.POST.get('heading', ''),
        'subheading1': request.POST.get('subheading1', ''),
        'subheading2': request.POST.get('subheading2', ''),
        'subheading3': request.POST.get('subheading3', ''),
        'desc1': request.POST.get('desc1', ''),
        'desc2': request.POST.get('desc2', ''),
        'desc3': request.POST.get('desc3', ''),
    }
    try:
        updated = CmsAbout.objects.update(**data)
        if not updated:
            CmsAbout.objects.create(**data)
        return JsonResponse({'status': True, 'msg': 'Data Saved'})
    except Exception as e:
        return JsonResponse({'status': False, 'msg': str(e)})


# ─── CMS - Settings ─────────────────────────────────────────────────────────

@admin_login_required
def setting_page(request):
    settings_data = CmsSetting.objects.all()
    return render(request, 'admin/setting_page.html', {'setting_page_data': settings_data})


@admin_login_required
@require_POST
def insert_setting_page_data(request):
    existing_logo = request.POST.get('website_logo_recent_photo', '')
    logo = handle_upload(request, 'website_logo', 'web', existing_logo)

    data = {
        'website_title': request.POST.get('website_title', ''),
        'email1': request.POST.get('email1', ''),
        'email2': request.POST.get('email2', ''),
        'phone1': request.POST.get('phone1', ''),
        'phone2': request.POST.get('phone2', ''),
        'fb_link': request.POST.get('fb_link', ''),
        'twitter_link': request.POST.get('twitter_link', ''),
        'youtube_link': request.POST.get('youtube_link', ''),
        'linkdin_link': request.POST.get('linkdin_link', ''),
        'instagram_link': request.POST.get('instagram_link', ''),
        'website_meta_keyword': request.POST.get('website_meta_keyword', ''),
        'website_meta_desc': request.POST.get('website_meta_desc', ''),
        'gtag': request.POST.get('gtag', ''),
        'facebook_anylatics': request.POST.get('facebook_anylatics', ''),
        'website_address': request.POST.get('website_address', ''),
        'website_logo': logo,
    }
    try:
        updated = CmsSetting.objects.update(**data)
        if not updated:
            CmsSetting.objects.create(**data)
        return JsonResponse({'status': True, 'msg': 'Data Saved'})
    except Exception as e:
        return JsonResponse({'status': False, 'msg': str(e)})