from django.urls import include, path
from . import views
from django.views.generic.base import RedirectView
from . import apis

# アプリケーションの名前空間
# https://docs.djangoproject.com/ja/2.0/intro/tutorial03/
app_name = 'web'

urlpatterns = [
    path('', views.index, name='index'),
]
