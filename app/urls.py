from django.urls import re_path,path,include
from .views import register,index,loginPage,projectUpload,logout_user,profile,EditProfileView,rate_project,single_project,search_project,ProfileList,PostList,UserViewSet
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers

router = routers.DefaultRouter()
router.register('users',UserViewSet)
 
urlpatterns = [
    re_path(r'^$', index , name='home'),
    path('register/', register, name='register'),
    path('login/', loginPage, name='login'),
    path('api/', include(router.urls)),
    path('post/', projectUpload ,  name='projectUpload'),
    path('logout/',logout_user,name='logout'),
    path('profile/<int:id>/', profile, name="profile"),
    path('edit/<int:id>/',EditProfileView.as_view(), name="edit"),
    path('rate_project/<int:id>/',rate_project, name='rate_project'),
    path('single_project/<int:id>/',single_project, name='single_project'),
    path('search_project/', search_project , name='search_project'),
    re_path(r'^api/profile/$', ProfileList.as_view()),
    re_path(r'^api/post/$', PostList.as_view()),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)