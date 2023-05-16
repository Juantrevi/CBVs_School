

from django.contrib import admin
from django.urls import path, include
from APP_CBSs import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='index'),
    path('basic_app/', include('APP_CBSs.urls', namespace='APP_CBSs'))
]

