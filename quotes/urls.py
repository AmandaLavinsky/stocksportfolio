from django.urls import path
#Importar o arquivo views.py para ser utilizado na urls.py
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('news.html',views.news,name="news"),
    path('add_stock.html', views.add_stock,name='add_stock'),
    path('delete/<stock_id>',views.delete,name='delete'),
    path('delete_stock',views.delete_stock,name='delete_stock'),
    path('search_news.html',views.search_news,name='search_news'),
    path('add_upperlimit.html',views.add_upperlimit,name='add_upperlimit'),
    path('add_lowerlimit.html',views.add_lowerlimit,name='add_lowerlimit'),
]