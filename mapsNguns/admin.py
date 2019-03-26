from django.contrib import admin

from .models import Map, City, Weapon, Vehicle, MapImage, WeaponImage

admin.site.register(Map)
admin.site.register(City)
admin.site.register(Weapon)
admin.site.register(Vehicle)
admin.site.register(MapImage)
admin.site.register(WeaponImage)
