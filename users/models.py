from django.db import models
from django.contrib.auth.models import User
from django.utils.text import gettext_lazy as _
from PIL import Image


class Profile(models.Model):
    gender_choice = (
        ('M', 'male'),
        ('F', 'female'),
        ('O', 'other')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_('User'))
    pubg_id = models.IntegerField(unique=True, blank=True, null=True, verbose_name=_('Pubg ID'))
    name = models.CharField(max_length=25, verbose_name=_('Name'))
    age = models.PositiveIntegerField(verbose_name=_('Age'))
    gender = models.CharField(choices=gender_choice, max_length=1, verbose_name=_('Gender'))
    image = models.ImageField(default='default.jpg', upload_to='profile_pics', verbose_name=_('User image'))

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super(Profile, self).save()
        image = Image.open(self.image.path)
        if image.height > 300 and image.width > 300:
            output_size = (300, 300)
            image.thumbnail(output_size)
            image.save(self.image.path)

    class Meta:
        verbose_name = _('Pubg Profile')
        verbose_name_plural = _('Pubg Profiles')
