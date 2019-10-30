from django.urls import path

from . import views
app_name='giaodien'
urlpatterns = [
    #path('', views.giaodien, name='giaodien'),
    path('index/', views.index, name='index'),
    path('giaodien/', views.giaodien, name='giaodien'),


]