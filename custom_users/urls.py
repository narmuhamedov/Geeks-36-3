from django.urls import path
from . import views

app_name = 'persons'
urlpatterns = [
    path('register/', views.RegistrationView.as_view(), name='register'),
    path('login/', views.InLoginView.as_view(), name='login'),
    path('logout/', views.OutLogoView.as_view(), name='logout'),
    path('user_list/', views.UserListView.as_view(), name='person_list')
]
