from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import handler404, handler500

urlpatterns = [
    # Admin honeypot
    path('admin/', include('admin_honeypot.urls')),
    path('securelogin/', admin.site.urls),
    path('', include('store.urls', namespace='store')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('management/', include('management.urls', namespace='management')),
    path('contact/', include('contact.urls', namespace='contact')),
]

handler404 = "errors.views.error_404"

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_URL)