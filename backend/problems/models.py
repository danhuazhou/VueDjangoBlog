from django.db import models
from django.utils.timezone import now
from mdeditor.fields import MDTextField
from MyBlog.utils import cache, cache_decorator


# Create your models here.
class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    created_time = models.DateTimeField('创建时间', default=now)
    last_mod_time = models.DateTimeField('修改时间', default=now)

    class Meta:
        abstract = True


class Problems(BaseModel):
    """题库"""
    EASY = 'E'
    MEDIUM = 'M'
    HARD = 'H'
    DIFFICULTY_CHOICES = (
        (EASY, '容易'),
        (MEDIUM, '中等'),
        (HARD, '困难'),
    )
    title = models.CharField('题目', max_length=200)
    description = MDTextField('题目描述')
    solution = MDTextField('题解')

    difficulty = models.CharField('难度', max_length=2,
                                  choices=DIFFICULTY_CHOICES, default=EASY)
    category = models.ForeignKey('Category', verbose_name='分类',
                                 on_delete=models.CASCADE, blank=False,
                                 null=False)
    tags = models.ManyToManyField('Tag', verbose_name='标签集合', blank=True)
    url = models.URLField('题目链接')
    website = models.CharField('网站', max_length=50)
    review_time = models.DateTimeField('复习时间')
    successes = models.PositiveSmallIntegerField('成功次数')
    failtures = models.PositiveSmallIntegerField('失败次数')
    order = models.IntegerField('排序', blank=False, null=False, default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-order', '-review_time',)
        verbose_name = "文章"
        verbose_name_plural = verbose_name
        get_latest_by = 'id'
        db_table = 'problems_problems'


class Tag(BaseModel):
    """题目标签"""
    name = models.CharField('标签名', max_length=30, unique=True)
    slug = models.SlugField(default='no-slug', max_length=60, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = "标签"
        verbose_name_plural = verbose_name
        db_table = 'problems_tag'


class Category(BaseModel):
    """题目分类"""
    name = models.CharField('分类名', max_length=30, unique=True)
    parent_category = models.ForeignKey('self', verbose_name="父级分类",
                                        blank=True, null=True,
                                        on_delete=models.CASCADE,
                                        related_name="sub_category")
    slug = models.SlugField(default='no-slug', max_length=60, blank=True)

    class Meta:
        ordering = ['name']
        verbose_name = "分类"
        verbose_name_plural = verbose_name
        db_table = 'problems_category'

    def __str__(self):
        return self.name
