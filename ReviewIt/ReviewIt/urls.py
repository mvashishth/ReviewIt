from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('webapp/', include('webapp.urls')),
    path('admin/', admin.site.urls),
]