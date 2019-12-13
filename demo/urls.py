from django.http import HttpResponse
from django.urls import path, include


def home(request):
    return HttpResponse(
        "Welcome to ScanAPI Demo."
        "\n\nAccess the demo api at: https://demo.scanapi.dev/api"
    )


urlpatterns = [path("", home, name="index"), path("api/", include("demo.api.urls"))]
