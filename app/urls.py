from django.urls import re_path,path
from .views import register,index,loginPage,rate_image,projectUpload,logout_user,profile,EditProfileView,rate_design,rate_context
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    re_path(r'^$', index , name='home'),
    path('register/', register, name='register'),
    path('login/', loginPage, name='login'),
    path('rate/',rate_image,name='rate-view'),
    path('post/', projectUpload ,  name='projectUpload'),
    path('logout/',logout_user,name='logout'),
    path('profile/<int:id>/', profile, name="profile"),
    path('edit/<int:pk>/',EditProfileView.as_view(), name="edit"),
    path('rate_design/<int:id>',rate_design,name='rate_design'),
    path('rate_context/<int:id>',rate_context,name='rate_context')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)