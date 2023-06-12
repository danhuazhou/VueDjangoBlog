from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    """
    评论序列化
    """

    class Meta:
        model = Comment
        fields = "__all__"
