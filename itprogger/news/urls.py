from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_home, name='home'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.NewsDatailView.as_view(), name='news-detail')
]