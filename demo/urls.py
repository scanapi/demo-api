from django.contrib import admin
from django.shortcuts import redirect
from django.urls import include, path


urlpatterns = [
    path("", lambda req: redirect("/api/v1/")),
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    # DEPRECATED: the old demo api. We are leaving it here only to avoid breaking external code
    # that depends on it.
    path("api/", include("api.urls")),
    path("api/<str:version>/", include("snippets.urls")),
]
