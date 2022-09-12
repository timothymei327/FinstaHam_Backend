from django.conf.urls import include
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('unmrkd.urls')),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework'))
]
