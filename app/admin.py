from django.contrib import admin
from app.models import Event, Speaker, Sponsor, Gallery, SponsorCategory, Items, PAYMENT, EventRegisterForm

admin.site.register(Event)
admin.site.register(Items)
admin.site.register(Speaker)
admin.site.register(Sponsor)
admin.site.register(SponsorCategory)
admin.site.register(Gallery)
admin.site.register(PAYMENT)
admin.site.register(EventRegisterForm)
