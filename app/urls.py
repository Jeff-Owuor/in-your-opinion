from django.urls import re_path,path
from .views import register,index,loginPage

urlpatterns = [
    re_path(r'^$', index , name='home'),
    path('register/', register, name='register'),
    path('login/', loginPage, name='login'),
]