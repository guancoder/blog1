# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import *
import math

from django.core.paginator import Paginator
# Create your views here.
def showAll(request,num=1):

    #获取当前页码数
    num = int(num)

    #1.查询所有的帖子
    posts = Post.objects.order_by('-created')

    #2.创建分页器对象
    paginator = Paginator(posts,per_page=1)

    #3.获取当前页的数据
    page_posts = paginator.page(num)

    #4.每页显示页码的范围
    begin = (num - int(math.ceil(10.0/2)))
    if begin < 1:
        begin = 1
    #每页结束码
    end = begin + 9
    if end > paginator.num_pages:
        end = paginator.num_pages
    if end <= 10:
        begin = 1
    else:
        begin = end - 9
    pagelist = range(begin,end + 1)
    return render(request,'index.html',{'posts':page_posts,'pagelist':pagelist,'currentNum':num})

#查看帖子内容
def detail(request,postid):
    postid = int(postid)

    #根据帖子id查看帖子的详细内容
    post = Post.objects.filter(id = postid)


    return render(request,'detail.html',{'post':post})

#根据类别查询帖子
def getPostsByCid(request,cid):

    cid = int(cid)
    posts = Post.objects.filter(category=cid)
    return render(request,'result.html',{'posts':posts})


def getPostsByCreated(request,year,month):
    #根据发帖时间查找帖子信息
    posts = Post.objects.filter(created__year=year,created__month=month)
    return render(request,'result.html',{'posts':posts})