from django.contrib import admin

# Register your models here.

from boltstream.models import Stream


@admin.register(Stream)
class StreamAdmin(admin.ModelAdmin):
    list_display = ("__str__", "started_at", "is_live")
    readonly_fields = ("hls_url",)


