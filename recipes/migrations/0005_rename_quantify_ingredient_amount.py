# Generated by Django 5.0.2 on 2024-04-01 20:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_remove_recipes_intensidade_recipes_intensity_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingredient',
            old_name='quantify',
            new_name='amount',
        ),
    ]
