# Generated by Django 5.0.2 on 2024-03-19 20:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_recipes_intensidade'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipes',
            name='intensidade',
        ),
        migrations.AddField(
            model_name='recipes',
            name='intensity',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='recipes',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='recipes',
            name='preparation',
            field=models.TextField(),
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('quantify', models.IntegerField(default=1)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredients', to='recipes.recipes')),
            ],
        ),
    ]