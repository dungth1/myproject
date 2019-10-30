from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from tutorials import views
app_name = 'tutorials'

urlpatterns = [
    path('',include('login.urls')),
    path('databases/upload/', views.uploadTutorial, name='upload_tutorial'),
    path('databases/', views.tutorialList, name='tutorial_list'),
    path('databases/<int:pk>', views.deleteTutorial, name='tutorial'),
    path('databases/edit/<int:pk>', views.approveTutorial, name='approveTutorial'),
   # path('databases/edit/<int:pk>', views.approveTutorial, name='approveTutorial'),
    path('admin/', admin.site.urls),

]

if settings.DEBUG:  # remember to set 'DEBUG = True' in settings.py
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
