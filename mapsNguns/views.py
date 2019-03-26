from django.views import generic

from .models import Map, City, Vehicle, Weapon


class MapListView(generic.ListView):
    queryset = Map.objects.all()
    template_name = "mapsNguns/list-map.html"


class MapWeaponListView(generic.ListView):
    queryset = Map.objects.all()
    template_name = "mapsNguns/list-map.html"

    def get_queryset(self):
        qs = super(MapWeaponListView, self).get_queryset()
        weapon = Weapon.objects.get(pk=self.kwargs.get('pk'))
        if weapon:
            return qs.filter(weapon=weapon)
        return qs


class CityListView(generic.ListView):
    queryset = City.objects.all()
    template_name = "mapsNguns/list-city.html"

    def get_queryset(self):
        qs = super(CityListView, self).get_queryset()
        map = Map.objects.get(pk=self.kwargs.get('pk'))
        if map:
            return qs.filter(map=map)
        return qs


class VehicleListView(generic.ListView):
    queryset = Vehicle.objects.all()
    template_name = "mapsNguns/list-vehicle.html"


class WeaponListView(generic.ListView):
    queryset = Weapon.objects.all()
    template_name = "mapsNguns/list-weapon.html"


class WeaponDetailView(generic.DetailView):
    queryset = Weapon.objects.all()
    template_name = "mapsNguns/detail-weapons.html"
    context_object_name = "weapon"


class WeaponView(generic.TemplateView):
    template_name = "mapsNguns/demo.html"
