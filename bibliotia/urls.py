from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('securelogin/', admin.site.urls),
    path('', include('store.urls', namespace='store')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('management/', include('management.urls', namespace='management')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)