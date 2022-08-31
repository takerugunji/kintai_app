from django.contrib import admin
from .models import SubmitAttendance

# モデルをDjango管理画面で管理できるようにする
class AdminCustomize(admin.ModelAdmin):
    list_display = ('staff', 'place', 'in_out', 'time', 'date')

admin.site.register(SubmitAttendance, AdminCustomize)