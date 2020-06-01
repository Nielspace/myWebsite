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
             
             'content',
             'content1',
             'content2',

             'date_time',)