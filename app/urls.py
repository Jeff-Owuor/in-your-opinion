from django.urls import re_path,path
from .views import register,index,loginPage,projectUpload,logout_user,profile,EditProfileView,rate_project,single_project
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    re_path(r'^$', index , name='home'),
    path('register/', register, name='register'),
    path('login/', loginPage, name='login'),
    path('post/', projectUpload ,  name='projectUpload'),
    path('logout/',logout_user,name='logout'),
    path('profile/<int:id>/', profile, name="profile"),
    path('edit/<int:pk>/',EditProfileView.as_view(), name="edit"),
    path('rate_project/<int:id>/',rate_project, name='rate_project'),
    path('single_project/<int:id>/',single_project, name='single_project'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)