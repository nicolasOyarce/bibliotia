from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls', namespace='store')),
    #path('', include('books.urls')),
    path('accounts/', include('accounts.urls')),
    path('contact/', include('contact.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)