from .models import CmsSetting


def site_settings(request):
    """Inject CmsSetting and session user into every template context."""
    try:
        setting = CmsSetting.objects.first()
    except Exception:
        setting = None

    from django.conf import settings as django_settings
    return {
        'site_setting': setting,
        'admin_user': request.session.get('onepixel'),
        'MEDIA_URL': django_settings.MEDIA_URL,
    }
