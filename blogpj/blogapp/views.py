# 어떤 html을 보여줄지 설정하는 곳
from django.shortcuts import render
from .models import Post


def post_list(request):
    qs = Post.objects.all()  # QuerySet
    return render(request, 'blogapp/post_list.html', {
        'post_list': qs,
    })