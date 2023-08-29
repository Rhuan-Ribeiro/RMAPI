# Generated by Django 4.2.4 on 2023-08-23 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_character_origin_alter_character_charatertype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='species',
            field=models.CharField(blank=True, choices=[('human', 'HUMAN'), ('alien', 'ALIEN')], max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='status',
            field=models.CharField(blank=True, choices=[('alive', 'ALIVE'), ('dead', 'DEAD'), ('unknown', 'UNKNOWN')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='locationType',
            field=models.CharField(blank=True, choices=[('planet', 'PLANET'), ('cluster', 'CLUSTER'), ('space_station', 'SPACE STATION'), ('microverse', 'MICROVERSE'), ('tv', 'TV'), ('resort', 'RESORT'), ('fantasy_town', 'FANTASY TOWN')], max_length=100, null=True),
        ),
    ]