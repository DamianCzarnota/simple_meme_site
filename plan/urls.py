"""
URL configuration for plan project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from meme_site.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', meme_site_login.as_view(), name='login'),
    path('logout/',LogoutView.as_view(next_page='home'),name='logout'),
    path('upload/', meme_site_post_meme.as_view(), name='upload'),
    path('image/<int:pk>/', meme_site_image_details.as_view(), name='meme'),
    path('register/', meme_site_register.as_view(), name='register'),
    path('user/<str:username>/', meme_site_user_profile.as_view(), name='user_profile'),
    path('like-image/<int:pk>/', meme_site_like_image.as_view(), name='like_image'),
    path("", meme_site_main.as_view(), name="home"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)