from rest_framework import serializers
from backend.blog.models import Article


class ArticleSerilalizer(serializers.ModelSerializer):
    """
    创建序列化器
    """

    class Meta:
        model = Article
        fields = '__all__'
