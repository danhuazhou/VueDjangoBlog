from rest_framework import serializers
from backend.blog.models import Article, Category


class CategorySerializer(serializers.ModelSerializer):
    """
    类别序列化器
    """
    class Meta:
        model = Category
        fields = '__all__'


class ArticleSerilalizer(serializers.ModelSerializer):
    """
    创建序列化器
    """
    category = CategorySerializer()

    # category =
    class Meta:
        model = Article
        fields = '__all__'

# class ArticleDetailSerilalizer(serializers.ModelSerializer):
#     """
#     创建序列化器
#     """
#
#     class Meta:
#         model = Article
#         fields = '__all__'
