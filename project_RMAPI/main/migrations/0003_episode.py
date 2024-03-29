# Generated by Django 4.2.4 on 2023-08-22 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('air_date', models.DateField()),
                ('episode', models.CharField(max_length=150)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
