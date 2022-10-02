from django.http import HttpResponse

from coffee_app.models import Coffee


def coffee_app(request):
    q = Coffee.objects.all()
    return HttpResponse(q)

