from django.contrib import admin

from .models import *

admin.site.register(Registrations)

from .models import teacherreg
admin.site.register(teacherreg)
admin.site.register(Attendence)
admin.site.register(mark)
admin.site.register(leave)
admin.site.register(stdleave)
admin.site.register(timetable)
