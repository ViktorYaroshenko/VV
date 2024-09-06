# Generated by Django 5.1 on 2024-08-22 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='category',
            field=models.CharField(choices=[('poem', 'Стихотворение'), ('song', 'Песня'), ('story', 'Рассказ')], default='poem', max_length=10),
        ),
    ]
