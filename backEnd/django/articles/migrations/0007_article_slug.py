# Generated by Django 3.0.6 on 2020-05-31 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_auto_20200531_1506'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(blank=True, default=''),
        ),
    ]
