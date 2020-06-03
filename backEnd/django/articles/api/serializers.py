from rest_framework import serializers

from articles.models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
         model = Article
         fields = (
             'id',
             'title',
             'description',
             'image',
             'image1',
             'image2',
             'image3',
             
             'content',
             'content1',
             'content2',
             'content3',

             'date_time',)