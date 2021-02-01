from django.contrib import admin
from .models import *

admin.site.register(CustomUser)
admin.site.register(Chief)
admin.site.register(Assistant)
admin.site.register(Waiter)
