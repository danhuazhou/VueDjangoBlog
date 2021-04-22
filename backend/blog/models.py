import logging
from django.db import models
from mdeditor.fields import MDTextField
from django.utils.timezone import now
from django.urls import reverse
from django.conf import settings
from MyBlog.utils import cache, cache_decorator

logger = logging.getLogger(__name__)


# Create your models here.

class Article(object):
    """
    文章
    """
    DRAFT = 'DR'
    PUBLISH = 'PU'
    OPEN = 'OP'
    CLOSE = 'CL'
    STATUS_CHOICES = (
        (DRAFT, '草稿'),
        (PUBLISH, '发表'),
    )
    COMMENT_STATUS = (
        (OPEN, '打开'),
        (CLOSE, '关闭'),
    )
    title = models.CharField('标题', max_length=200, unique=True)
    body = MDTextField('正文')
    publish_time = models.DateTimeField('发布时间', blank=False, null=False, default=now)
    status = models.CharField('文章状态', max_length=2, choices=STATUS_CHOICES, default=PUBLISH)
    comment_status = models.CharField('评论状态', max_length=2, choices=COMMENT_STATUS, default=OPEN)
    # type = models.CharField('类型', max_length=1, choices=TYPE, default='a')
    type = models.CharField('类型')
    views = models.PositiveIntegerField('浏览量', default=0)
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='作者', blank=False, null=False,
    #                            on_delete=models.CASCADE)
    author = models.CharField()
    article_order = models.IntegerField('排序,数字越大越靠前', blank=False, null=False, default=0)
    category = models.ForeignKey('Category', verbose_name='分类', on_delete=models.CASCADE, blank=False, null=False)
    # tags = models.ManyToManyField('Tag', verbose_name='标签集合', blank=True)
    tags = models.CharField()

    def body_to_string(self):
        return self.body

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-article_order', '-pub_time']
        verbose_name = "文章"
        verbose_name_plural = verbose_name
        get_latest_by = 'id'

    def get_absolute_url(self):
        return reverse('blog:detailbyid', kwargs={
            'article_id': self.id,
            'year': self.created_time.year,
            'month': self.created_time.month,
            'day': self.created_time.day
        })

    @cache_decorator(60 * 60 * 10)
    def get_category_tree(self):
        tree = self.category.get_category_tree()
        names = list(map(lambda c: (c.name, c.get_absolute_url()), tree))

        return names

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def viewed(self):
        self.views += 1
        self.save(update_fields=['views'])

    def comment_list(self):
        cache_key = 'article_comments_{id}'.format(id=self.id)
        value = cache.get(cache_key)
        if value:
            logger.info('get article comments:{id}'.format(id=self.id))
            return value
        else:
            comments = self.comment_set.filter(is_enable=True)
            cache.set(cache_key, comments, 60 * 100)
            logger.info('set article comments:{id}'.format(id=self.id))
            return comments

    def get_admin_url(self):
        info = (self._meta.app_label, self._meta.model_name)
        return reverse('admin:%s_%s_change' % info, args=(self.pk,))

    @cache_decorator(expiration=60 * 100)
    def next_article(self):
        # 下一篇
        return Article.objects.filter(id__gt=self.id, status='p').order_by('id').first()

    @cache_decorator(expiration=60 * 100)
    def prev_article(self):
        # 前一篇
        return Article.objects.filter(id__lt=self.id, status='p').first()
