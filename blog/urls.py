from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.blog_view, name='blog'),
    # path('tel/', views.telefone_view, name='tel'),
]
