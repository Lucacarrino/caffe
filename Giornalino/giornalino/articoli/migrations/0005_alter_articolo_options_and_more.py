# Generated by Django 4.2.17 on 2025-01-16 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articoli', '0004_newslettersubscriber'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articolo',
            options={'ordering': ['-data_pubblicazione'], 'verbose_name': 'Articolo', 'verbose_name_plural': 'Articoli'},
        ),
        migrations.AlterModelOptions(
            name='newslettersubscriber',
            options={'verbose_name': 'Iscritto', 'verbose_name_plural': 'Iscritti'},
        ),
    ]
