from django.urls import path, re_path
from blog import views


urlpatterns = [
    re_path('', views.test_view, name='test')
]
