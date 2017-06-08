# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
# Register your models here.
from models import *

# Register your models here.
admin.site.register(identifier, admin.ModelAdmin)
admin.site.register(locations, admin.ModelAdmin)
admin.site.register(reviews, admin.ModelAdmin)
admin.site.register(user_logs, admin.ModelAdmin)
admin.site.register(occupants, admin.ModelAdmin)
admin.site.register(properties, admin.ModelAdmin)
admin.site.register(properties_log, admin.ModelAdmin)

