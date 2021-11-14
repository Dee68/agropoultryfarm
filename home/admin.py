from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Setting)
admin.site.register(SubscribedUser)
admin.site.register(ContactMessage)
admin.site.register(MailMessage)
