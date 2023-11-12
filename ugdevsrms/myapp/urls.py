from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),  # replace 'myapp' with the name of your app
]
# Path: ugdevsrms/myapp/urls.py

urlpatterns = [
    path('', views.my_view, name='my_view'),
]
