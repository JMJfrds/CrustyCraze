from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from Bread_Bakery import settings

app_name = 'bv1'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bv1/', include('bv1.urls')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

