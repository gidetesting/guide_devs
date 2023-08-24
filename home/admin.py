from django.contrib import admin
from home.models import info,basic,intermediate,premium

# Register your models here.
admin.site.register(info)
admin.site.register(basic)
admin.site.register(intermediate)
admin.site.register(premium)