from django.db import models


class Banner(models.Model):
    banner_name = models.CharField(max_length=255)
    banner_img = models.CharField(max_length=255, blank=True, default='')
    status = models.CharField(max_length=1, default='1')

    class Meta:
        db_table = 'banner'

    def __str__(self):
        return self.banner_name


class Donation(models.Model):
    donation_name = models.CharField(max_length=255)
    description = models.TextField(blank=True, default='')
    donation_img = models.CharField(max_length=255, blank=True, default='')
    status = models.CharField(max_length=1, default='1')

    class Meta:
        db_table = 'donation'

    def __str__(self):
        return self.donation_name


class Events(models.Model):
    events_name = models.CharField(max_length=255)
    about_events = models.TextField(blank=True, default='')
    events_content = models.TextField(blank=True, default='')
    events_img = models.CharField(max_length=255, blank=True, default='')
    events_banner_img = models.CharField(max_length=255, blank=True, default='')
    status = models.CharField(max_length=1, default='1')

    class Meta:
        db_table = 'events'

    def __str__(self):
        return self.events_name


class Role(models.Model):
    name = models.CharField(max_length=255)
    permission_ids = models.TextField(blank=True, default='')
    entry_date_time = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=1, default='1')

    class Meta:
        db_table = 'role'

    def __str__(self):
        return self.name


class PermissionType(models.Model):
    view_name = models.CharField(max_length=255)
    status = models.CharField(max_length=1, default='1')

    class Meta:
        db_table = 'permission_type'

    def __str__(self):
        return self.view_name


class Permission(models.Model):
    name = models.CharField(max_length=255)
    permission_type_id = models.IntegerField()
    status = models.CharField(max_length=1, default='1')

    class Meta:
        db_table = 'permission'

    def __str__(self):
        return self.name


class Staff(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    photo = models.CharField(max_length=255, blank=True, default='')
    role_id = models.IntegerField(null=True, blank=True)
    mobile_no = models.CharField(max_length=20, blank=True, default='')
    email_id = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    address = models.TextField(blank=True, default='')
    access_level = models.CharField(max_length=50, blank=True, default='')
    status = models.CharField(max_length=1, default='1')

    class Meta:
        db_table = 'staff'

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    testimonial_name = models.CharField(max_length=255)
    description = models.TextField(blank=True, default='')
    occupation = models.CharField(max_length=255, blank=True, default='')
    testimonial_img = models.CharField(max_length=255, blank=True, default='')
    status = models.CharField(max_length=1, default='1')

    class Meta:
        db_table = 'testimonial'

    def __str__(self):
        return self.testimonial_name


class Volunteer(models.Model):
    volunteer_name = models.CharField(max_length=255)
    volunteer_img = models.CharField(max_length=255, blank=True, default='')
    status = models.CharField(max_length=1, default='1')

    class Meta:
        db_table = 'volunteer'

    def __str__(self):
        return self.volunteer_name


class Team(models.Model):
    name = models.CharField(max_length=255)
    photo = models.CharField(max_length=255, blank=True, default='')
    designation = models.CharField(max_length=255, blank=True, default='')
    status = models.CharField(max_length=1, default='1')

    class Meta:
        db_table = 'team'

    def __str__(self):
        return self.name


class ContactEnquiry(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, default='')
    message = models.TextField(blank=True, default='')
    created_date = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'contact_enquiry'

    def __str__(self):
        return f"{self.name} - {self.email}"


class DonationEnquiry(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, blank=True, default='')
    email = models.EmailField(blank=True, default='')
    image = models.CharField(max_length=255, blank=True, default='')
    created_date = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'donation_enquiry'

    def __str__(self):
        return self.name


class CmsAbout(models.Model):
    heading = models.CharField(max_length=255, blank=True, default='')
    subheading1 = models.CharField(max_length=255, blank=True, default='')
    subheading2 = models.CharField(max_length=255, blank=True, default='')
    subheading3 = models.CharField(max_length=255, blank=True, default='')
    desc1 = models.TextField(blank=True, default='')
    desc2 = models.TextField(blank=True, default='')
    desc3 = models.TextField(blank=True, default='')

    class Meta:
        db_table = 'cms_about'

    def __str__(self):
        return self.heading


class CmsSetting(models.Model):
    website_title = models.CharField(max_length=255, blank=True, default='')
    email1 = models.CharField(max_length=255, blank=True, default='')
    email2 = models.CharField(max_length=255, blank=True, default='')
    phone1 = models.CharField(max_length=20, blank=True, default='')
    phone2 = models.CharField(max_length=20, blank=True, default='')
    fb_link = models.CharField(max_length=500, blank=True, default='')
    twitter_link = models.CharField(max_length=500, blank=True, default='')
    youtube_link = models.CharField(max_length=500, blank=True, default='')
    linkdin_link = models.CharField(max_length=500, blank=True, default='')
    instagram_link = models.CharField(max_length=500, blank=True, default='')
    website_meta_keyword = models.TextField(blank=True, default='')
    website_meta_desc = models.TextField(blank=True, default='')
    gtag = models.TextField(blank=True, default='')
    facebook_anylatics = models.TextField(blank=True, default='')
    website_address = models.TextField(blank=True, default='')
    website_logo = models.CharField(max_length=255, blank=True, default='')

    class Meta:
        db_table = 'cms_setting'

    def __str__(self):
        return self.website_title
