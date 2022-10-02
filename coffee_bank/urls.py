from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from coffee_app.views import coffee_app

urlpatterns = [
  path('admin/', admin.site.urls),
  path('', coffee_app),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

