from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path("admin/", admin.site.urls),
    # DEPRECATED: the old demo api. We are leaving it here only to avoid breaking external code
    # that depends on it.
    path("api/", include("api.urls")),
    path("", include("snippets.urls")),
]


## Authentication URLs
urlpatterns += [
    path("api-auth/", include("rest_framework.urls")),
    path("api-token-auth/", obtain_auth_token, name="api_token_auth"),
    path("rest-auth/registration/", include("rest_auth.registration.urls")),
]
