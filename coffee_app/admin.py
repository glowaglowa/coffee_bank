from django.contrib import admin
from django.urls import path

from coffee_app.models import Roastery, Origin, Roast, Coffee, Users, UsersCoffees
from coffee_app.views import coffee_app


admin.site.register(Roastery)
admin.site.register(Origin)
admin.site.register(Roast)
admin.site.register(Coffee)
admin.site.register(Users)
admin.site.register(UsersCoffees)

urlpatterns = [
  path('admin/', admin.site.urls),
  path('', coffee_app)
]