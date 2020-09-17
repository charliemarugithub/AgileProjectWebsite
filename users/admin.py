from django.contrib import admin

from .models import Profile, Subscription


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('firstName',
                    'lastName',
                    'username',
                    'sub_type',
                    'state',
                    'date_of_signup')

    def firstName(self, obj):
        return obj.firstName


admin.site.register(Profile)
admin.site.register(Subscription, SubscriptionAdmin)


