from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('news.html',views.news,name="news"),
    path('add_stock.html', views.add_stock,name='add_stock'),
    path('delete/<stock_id>',views.delete,name='delete'),
    path('delete_stock',views.delete_stock,name='delete_stock'),
    path('search_news.html',views.search_news,name='search_news'),
]