from django.contrib import admin
from .models import Supplier, Contract, Glaccount, Site

# Register your models here.
admin.site.register(Supplier)
admin.site.register(Contract)
admin.site.register(Glaccount)
admin.site.register(Site)



