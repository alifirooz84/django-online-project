from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('phoneapp.urls')),  # همه آدرس‌ها به اپ ما ارجاع داده میشه
]
