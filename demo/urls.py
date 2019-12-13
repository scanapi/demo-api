from django.http import HttpResponse
from django.urls import path, include


def home(request):
    return HttpResponse(
        "<h2>ScanAPI Demo</h2>"
        "<p>This is an application to help showing how ScanAPI works</p>"
        "<p>Access the demo API at: <a href=https://demo.scanapi.dev/api>https://demo.scanapi.dev/api</a></p>"
    )


urlpatterns = [path("", home, name="index"), path("api/", include("demo.api.urls"))]
