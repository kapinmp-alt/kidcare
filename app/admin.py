from .models import Nanny, Bio, UserProfile, Booking
from django.contrib import admin
from .models import Company
# Register your models here.


# Register your models here.
admin.site.register(Nanny)
admin.site.register(Bio)
admin.site.register(UserProfile)
admin.site.register(Company)
admin.site.register(Booking)

