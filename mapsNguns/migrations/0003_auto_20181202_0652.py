# Generated by Django 2.1.3 on 2018-12-02 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapsNguns', '0002_auto_20181202_0537'),
    ]

    operations = [
        migrations.AddField(
            model_name='weapon',
            name='bullet',
            field=models.CharField(blank=True, choices=[('5.56', '5.56mm'), ('9', '9mm'), ('7.82', '7.82mm'), ('12', '12mm')], max_length=255),
        ),
        migrations.AddField(
            model_name='weapon',
            name='modes',
            field=models.CharField(blank=True, choices=[('3', 'ABS'), ('2', 'AB/BS/AS'), ('1', 'S')], max_length=255),
        ),
        migrations.AddField(
            model_name='weapon',
            name='slots',
            field=models.PositiveIntegerField(default=1, verbose_name='No. of custom slots'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='weapon',
            name='type',
            field=models.CharField(choices=[('smg', 'Sub Machine Gun'), ('rifle', 'Rifle'), ('handgun', 'Hand Gun'), ('melee', 'Melee'), ('sniper', 'sniper')], default='melee', max_length=255),
        ),
    ]