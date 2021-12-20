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
<<<<<<< HEAD
    # path('api/v1/checkout', include('user.urls')),
    path('api/v1/users', include('user.urls'))
=======
    path('api/v1/', include('userinfo.urls'))
>>>>>>> ff0ab39d672c224977c2f9dcf7d6b15c923fda8c
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


