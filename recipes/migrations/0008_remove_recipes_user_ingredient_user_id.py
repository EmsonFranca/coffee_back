# Generated by Django 5.0.2 on 2024-04-14 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0007_rename_amount_ingredient_quantify_alter_recipes_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipes',
            name='user',
        ),
        migrations.AddField(
            model_name='ingredient',
            name='user_id',
            field=models.ImageField(default=1, upload_to=''),
        ),
    ]
