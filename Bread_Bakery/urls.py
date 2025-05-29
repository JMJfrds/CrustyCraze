
from django.contrib import admin
from django.urls import path, include


app_name = 'bv1'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bv1/', include('bv1.urls')),
]
