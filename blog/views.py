from django.shortcuts import render
from . import models


def blog_view(request):
    if request.method == 'GET':
        post = models.Blog.objects.all()
        tel = models.Telefone.objects.all()
        return render(request, template_name='blog.html',
                      context={'post': post,
                               'tel': tel,
                               })



# def telefone_view(request):
#     if request.method == 'GET':
#         tel = models.Telefone.objects.all()
#         return render(request, template_name='blog.html', context={'tel':tel})