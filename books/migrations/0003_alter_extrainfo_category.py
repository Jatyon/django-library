# Generated by Django 5.0.4 on 2024-05-11 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_alter_extrainfo_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extrainfo',
            name='category',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(2, 'Sci-fi'), (0, 'Powiesc'), (3, 'Dramat'), (1, 'Naukowa')], null=True),
        ),
    ]