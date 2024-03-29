# Generated by Django 4.2.4 on 2023-08-22 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_character_chratertype_alter_character_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='chraterType',
        ),
        migrations.AddField(
            model_name='character',
            name='charaterType',
            field=models.CharField(choices=[('genetic_experiment', 'GENETIC EXPERIMENT'), ('Superhuman (Ghost trains summoner)', 'SUPERHUMAN'), ('parasite', 'parasite')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='species',
            field=models.CharField(choices=[('human', 'HUMAN'), ('alien', 'ALIEN')], max_length=150, null=True),
        ),
    ]
