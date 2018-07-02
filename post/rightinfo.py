#coding=utf-8
from django.db.models import Count

from .models import *
def getRightInfo(request):
    #分类查询
    cate_posts = Post.objects.values('category','category__cname').annotate(c=Count('*')).order_by('-c')
    #归档
    from django.db import connection
    cursor = connection.cursor()
    cursor.execute('select created,count("*") as c from t_post group by date_format(created,"%Y-%m" )ORDER BY c DESC ')
    datas = cursor.fetchall()

    #近期文章
    recent_posts = Post.objects.order_by('-created')[:3]

    return {'cate_posts':cate_posts,'date_posts':datas,'recent_posts':recent_posts}