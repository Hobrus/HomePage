from django.contrib import admin

from .models import Good, Category

# Register your models here.
admin.site.register(Good)
admin.site.register(Category)