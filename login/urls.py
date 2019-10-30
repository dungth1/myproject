from django.urls import path
from .views import IndexClass, LoginClass, PhuonganClass, ViewUser, view_data, Phuongan_dhml, Phuongan_didong, Phuongan_tktu

from . import views

urlpatterns = [
    path('', IndexClass.as_view(),name='index'),

    path('login/', LoginClass.as_view(),name='login'),
    path('view_user/', ViewUser.as_view(),name='view_user'),
    path('view_data/', view_data,name='view_data'),
    path('phuongan/', PhuonganClass.as_view(),name='phuongan'),
    path('donvi/', views.donvi,name='donvi'),
    path('thunghiem/', views.thunghiem,name='thunghiem'),
    path('phuongan_didong/', Phuongan_didong.as_view(),name='phuongan_didong'),
    path('phuongan_tktu/', Phuongan_tktu.as_view(),name='phuongan_tktu'),
    path('phuongan_dhml/', Phuongan_dhml.as_view(),name='phuongan_dhml'),


]