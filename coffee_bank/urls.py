from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from coffee_app.views import CoffeesView, coffee_register_page, coffee_login_page, coffe_log_out, coffee_user_page

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', CoffeesView.as_view(), name="coffee_app"),
                  path('register/', coffee_register_page, name="registerPage"),
                  path('login/', coffee_login_page, name="loginPage"),
                  path('logout/', coffe_log_out, name="logoutPage"),
                  path('user/', coffee_user_page, name="coffeeUserPage"),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
