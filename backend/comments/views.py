from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import Comment
from .serialize import CommentSerializer


# Create your views here.
class CommentsViewSet(ModelViewSet):
    # queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        article_id = self.request.query_params.get('article', None)
        print('##########')
        print(self.request)
        print(self.request.query_params)
        print(article_id)
        queryset = Comment.objects.filter(id=article_id)
        return queryset
