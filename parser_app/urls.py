from django.urls import path
from . import views

urlpatterns = [
    path('parsing/', views.ParserFormView.as_view(), name='start_parser'),
]