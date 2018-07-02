# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

# Create your models here.
#类别
class Category(models.Model):
    cname = models.CharField(max_length=30,unique=True,verbose_name=u'类别名称')

    def __unicode__(self):
        return u'Category:%s'%self.cname

    class Meta:
        db_table = 't_category'
        verbose_name_plural =u'类别'


#标签
class Tag(models.Model):
    tname = models.CharField(max_length=30,unique=True,verbose_name=u'标签名称')

    def __unicode__(self):
        return u'Tag:%s' % self.tname

    class Meta:
        db_table = 't_tag'
        verbose_name_plural=u'标签'


#帖子
class Post(models.Model):
    title = models.CharField(max_length=100,unique=True,verbose_name=u'标题')
    content = RichTextUploadingField(verbose_name=u'内容')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name=u'所属类别')
    tag = models.ManyToManyField(Tag,verbose_name=u'标签')

    def __unicode__(self):
        return u'Post:%s' % self.title

    class Meta:
        db_table = 't_post'
        verbose_name_plural = u'帖子'
