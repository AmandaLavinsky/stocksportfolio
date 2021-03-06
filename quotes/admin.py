from django.contrib import admin
from .models import Stock,UpperLimit,LowerLimit
# Register your models here.

admin.site.register(Stock)
admin.site.register(UpperLimit)
admin.site.register(LowerLimit)
