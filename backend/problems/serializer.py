from rest_framework import serializers
from .models import Problems, Tag, Category

class CategorySerializer(serializers.ModelSerializer):
    """
    类别序列化器
    """
    class Meta:
        model = Category
        fields = '__all__'

class ProblemsSerilalizer(serializers.ModelSerializer):
    """
    创建序列化器
    """
    category = CategorySerializer()

    # category =
    class Meta:
        model = Problems
        fields = '__all__'
