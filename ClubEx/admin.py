from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from .models import Video


class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    list_display = ('category',
                    'video_name',
                    'video',
                    'content',
                    )

    def video(self, obj):
        return obj.category


admin.site.register(Video, MyModelAdmin)



