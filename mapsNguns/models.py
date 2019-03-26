from django.db import models
from django.utils.text import gettext_lazy as _

from PIL import Image

GENRE_CHOICES = (
    ("am", "AMBUSH"),
    ("sn", "SNIPING"),
    ("as", "ASSAULT"),
    ("st", "STEALTH"),
)

WEAPON_TYPE = (
    ("smg", "Sub Machine Gun"),
    ("rifle", "Rifle"),
    ("handgun", "Hand Gun"),
    ("melee", "Melee"),
    ("sniper", "sniper")
)

BULLET_TYPE = (
    ("5.56", "5.56mm"),
    ("9", "9mm"),
    ("7.82", "7.82mm"),
    ("12", "12mm"),
)

MODE_TYPE = (
    ("3", "ABS"),
    ("2", "AB/BS/AS"),
    ("1", "S")
)


class Map(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Map Name"))
    genre = models.CharField(max_length=255, choices=GENRE_CHOICES, blank=True)
    short_desc = models.TextField(verbose_name=_("Short Description"))
    long_desc = models.TextField(verbose_name=_("Long Description"))

    def __str__(self):
        return self.name

    def city_count(self):
        return str(self.city_set.all().count())

    class Meta:
        verbose_name_plural = _("Maps")


class Weapon(models.Model):
    maps = models.ManyToManyField(to=Map)
    name = models.CharField(max_length=255, verbose_name=_("Weapon Name"))
    type = models.CharField(max_length=255, choices=WEAPON_TYPE, default="melee")
    bullet = models.CharField(max_length=255, choices=BULLET_TYPE, blank=True)
    slots = models.PositiveIntegerField(verbose_name=_("No. of custom slots"))
    modes = models.CharField(max_length=255, choices=MODE_TYPE, blank=True)
    desc = models.TextField(verbose_name=_("Weapon Description"))
    damage = models.PositiveIntegerField(verbose_name=_("Damage level out of 5"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = _("Weapons")


class Vehicle(models.Model):
    maps = models.ManyToManyField(to=Map)
    name = models.CharField(max_length=255, verbose_name=_("Vehicle Name"))
    is_drivable = models.BooleanField(verbose_name=_("Is Drivable"), default=True)
    capacity = models.PositiveIntegerField(verbose_name=_("No. of seats"))
    desc = models.TextField(verbose_name=_("Description"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = _("Vehicles")


class City(models.Model):
    map = models.ForeignKey(to=Map, on_delete=models.PROTECT)
    name = models.CharField(max_length=255, verbose_name=_("City Name"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = _("Cities")


class MapImage(models.Model):
    map = models.ForeignKey(to=Map, on_delete=models.PROTECT)
    image = models.ImageField(upload_to="map_pics", verbose_name=_("Images"))

    def __str__(self):
        return self.map.name + "'s" + "Image"

    class Meta:
        verbose_name_plural = _("Map Images")

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super(MapImage, self).save()
        image = Image.open(self.image.path)
        if image.height > 300 and image.width > 300:
            output_size = (300, 300)
            image.thumbnail(output_size)
            image.save(self.image.path)


class WeaponImage(models.Model):
    weapon = models.ForeignKey(to=Weapon, on_delete=models.PROTECT)
    image = models.ImageField(upload_to="gun_pics", verbose_name=_("Images"))

    def __str__(self):
        return self.weapon.name + "'s" + "Image"

    class Meta:
        verbose_name_plural = _("Weapon Images")

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super(WeaponImage, self).save()
        image = Image.open(self.image.path)
        if image.height > 300 and image.width > 300:
            output_size = (300, 300)
            image.thumbnail(output_size)
            image.save(self.image.path)
