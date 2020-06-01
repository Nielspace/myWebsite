from django.db import models
from django.utils import timezone

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
import datetime
# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=1000, default = True) 
    image = models.ImageField(upload_to = 'uploads/', default = 'pic_folder/None/no-img.jpg')
    content = RichTextUploadingField(blank=True, null=True)
    date_time = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.title
