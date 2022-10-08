from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from coffee_app.views import CoffeesView

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', CoffeesView.as_view(), name="coffee_app"),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
