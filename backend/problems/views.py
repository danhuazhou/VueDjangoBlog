import os
import datetime

from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from mdeditor.views import UploadView, MDEDITOR_CONFIGS
import logging
from .models import Problems
from .serializer import ProblemsSerilalizer

logger = logging.getLogger(__name__)

# Create your views here.
@api_view(['GET'])
def api_root(request, format=None):
    return Response(
        {
            'test': reverse('test', request=request, format=format),
            'blogs': reverse('blogs-list', request=request, format=format),
            # 'user-list': reverse('user-list',request=request,format=format),
            # 'user-detail': reverse('user-detail',request=request,format=format),
            'user-detail': reverse('accounts:user-list', request=request,
                                   format=format),
        }
    )


class ProblemsViewSet(ModelViewSet):
    queryset = Problems.objects.all()
    serializer_class = ProblemsSerilalizer


class MdUploadView(UploadView):
    def post(self, request, *args, **kwargs):
        upload_image = request.FILES.get("editormd-image-file", None)
        media_root = settings.MEDIA_ROOT
        print(request)
        uid = request.user.uid
        print('#',uid)
        # image none check
        if not upload_image:
            return JsonResponse({
                'success': 0,
                'message': "未获取到要上传的图片",
                'url': ""
            })

        # image format check
        file_name_list = upload_image.name.split('.')
        file_extension = file_name_list.pop(-1)
        file_name = '.'.join(file_name_list)
        if file_extension not in MDEDITOR_CONFIGS['upload_image_formats']:
            return JsonResponse({
                'success': 0,
                'message': "上传图片格式错误，允许上传图片格式为：%s" % ','.join(
                    MDEDITOR_CONFIGS['upload_image_formats']),
                'url': ""
            })

        # image floder check
        media_root = os.path.join(media_root, uid.hex)  # 用户上传文件目录
        file_path = os.path.join(media_root, MDEDITOR_CONFIGS['image_folder'])
        if not os.path.exists(file_path):
            try:
                os.makedirs(file_path)
            except Exception as err:
                return JsonResponse({
                    'success': 0,
                    'message': "上传失败：%s" % str(err),
                    'url': ""
                })

        # save image
        file_full_name = '%s_%s.%s' % (file_name,
                                       '{0:%Y%m%d%H%M%S%f}'.format(
                                           datetime.datetime.now()),
                                       file_extension)
        with open(os.path.join(file_path, file_full_name), 'wb+') as file:
            for chunk in upload_image.chunks():
                file.write(chunk)

        return JsonResponse({'success': 1,
                             'message': "上传成功！",
                             'url': os.path.join(settings.MEDIA_URL,
                                                 uid.hex,
                                                 MDEDITOR_CONFIGS[
                                                     'image_folder'],
                                                 file_full_name)})
