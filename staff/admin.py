
from django.contrib import admin
from .models import contactModel, studentModel, roomModel,BookingModel
# Register your models here.
admin.site.register(contactModel)
admin.site.register(studentModel)
admin.site.register(roomModel)
admin.site.register(BookingModel)