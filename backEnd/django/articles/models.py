from django.db import models
from django.utils import timezone

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

from django.utils.text import slugify
# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=1000, default = True) 
    image = models.ImageField(upload_to='uploads/',height_field=None, width_field=None, max_length=100, default=None)
    content = RichTextUploadingField(blank=True, null=True)
    date_time = models.DateTimeField(default = timezone.now)


    def __str__(self):
        return self.title
