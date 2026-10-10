
from django.contrib import admin
from .models import Video


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "website_url")
    list_filter = ("category",)
    search_fields = ("title", "category")
    fields = ("title", "website_url", "category")
