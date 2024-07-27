from django.contrib import admin
from .models import Hydro, MHD, Scalar, RBC, CompressibleConvection

# Register your models here.

admin.site.register(Hydro)
admin.site.register(MHD)
admin.site.register(Scalar)
admin.site.register(RBC)
admin.site.register(CompressibleConvection)
