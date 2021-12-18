from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('admin/', admin.site.urls),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
    path('api/v1/', include('products.urls')),
    path('api/v1/orders', include('order.urls')),
    # path('api/v1/', include('review.urls')),
    # path('api/v1/checkout', include('user.urls')),
    path('api/v1/users', include('user.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
