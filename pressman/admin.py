from django.contrib import admin
from django.db import models
from pressman.models import PressMan, PressRelease

class PressManAdmin(admin.ModelAdmin):
    list_display = ('pr_name', 'pr_email', 'pr_url')
    
class PressReleaseAdmin(admin.ModelAdmin):
    list_display = ('pr_title', 'pr_body', 'pr_date_created')

    
admin.site.register(PressMan, PressManAdmin)
admin.site.register(PressRelease, PressReleaseAdmin)

