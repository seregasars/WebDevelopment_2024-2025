# main/admin.py
from django.contrib import admin
from .models import ContactMessage

# Регистрируем модель для отображения в админке
admin.site.register(ContactMessage)
