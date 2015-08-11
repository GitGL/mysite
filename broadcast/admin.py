from django.contrib import admin

# Register your models here.
from broadcast.models import Areas, Employees, TimeList, ApplyInfos

admin.site.register(Areas)
admin.site.register(Employees)
admin.site.register(TimeList)
admin.site.register(ApplyInfos)
