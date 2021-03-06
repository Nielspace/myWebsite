# Generated by Django 3.0.6 on 2020-06-01 16:52

import ckeditor_uploader.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='content1',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='content2',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='content3',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='date_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='article',
            name='description',
            field=models.CharField(default=' ', max_length=1000),
        ),
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, default=' ', upload_to='uploads/'),
        ),
        migrations.AddField(
            model_name='article',
            name='image1',
            field=models.ImageField(blank=True, default=' ', upload_to='uploads/'),
        ),
        migrations.AddField(
            model_name='article',
            name='image2',
            field=models.ImageField(blank=True, default=' ', upload_to='uploads/'),
        ),
        migrations.AddField(
            model_name='article',
            name='image3',
            field=models.ImageField(blank=True, default=' ', upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=500),
        ),
    ]
