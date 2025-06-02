from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('stocks.urls')),
    path('', include('accounts.urls')),
    path('', include('collection.urls')),
    path('', include('color.urls')),
    path('', include('sizes.urls')),
    path('', include('number.urls')),
    path('', include('brand.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
