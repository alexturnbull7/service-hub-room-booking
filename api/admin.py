from django.contrib import admin

# Register your models here.

from .models import Room
from .models import Status
from .models import UserType
from .models import Company
from .models import Profile
from .models import Booking

admin.site.register(Room)
admin.site.register(Profile)
admin.site.register(UserType)
admin.site.register(Company)
admin.site.register(Status)
admin.site.register(Booking)

