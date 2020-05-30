"""BlogProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, re_path
from django.conf.urls import url
from blog.views import MainPageView, SignUpView, LoginView, LogoutView, ProfileView, NewPostView, MyDeleteView, PostView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    re_path('signup', SignUpView.as_view(), name='signup'),
    re_path('login', LoginView.as_view(), name='login'),
    re_path('logout', LogoutView.as_view(), name='logout'),
    re_path('profile/', ProfileView.as_view(), name='profile'),
    re_path('newpost', NewPostView.as_view(), name='newpost'),
    re_path('posts/(?P<pid>\d+)', PostView.as_view(), name='post'),
    re_path('delete_post/(?P<pk>\d+)', MyDeleteView.as_view(), name='delete_post'),
    url(r'^$', MainPageView.as_view(), name='index'),
    re_path('index', MainPageView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
