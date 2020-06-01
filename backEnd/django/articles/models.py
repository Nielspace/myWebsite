from django.db import models
from django.utils import timezone

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
import datetime
# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=1000, default = ' ') 

    image = models.ImageField(upload_to = 'uploads/', default = 'empty', blank=True)
    content = RichTextUploadingField(blank=True, null=True)
    
    image1 = models.ImageField(upload_to = 'uploads/', default = 'empty1', blank=True)
    content1 = RichTextUploadingField(blank=True, null=True)

    image2 = models.ImageField(upload_to = 'uploads/', default = 'empty2', blank=False)
    content2 = RichTextUploadingField(blank=True, null=True)

    # image3 = models.ImageField(upload_to = 'uploads/', default = 'empty3', blank=True)
    # content3 = RichTextUploadingField(blank=True, null=True)


    date_time = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.title
