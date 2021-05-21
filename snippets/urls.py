from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.schemas import get_schema_view
from snippets import views

router = DefaultRouter()
router.get_api_root_view().cls.__name__ = "Snippets API"
router.get_api_root_view().cls.__doc__ = (
    "Snippets API was built for demo purposes of ScanAPI. "
    "API based on the Django REST Framework's tutorial."
)
router.register(r"health", views.HealthViewSet, basename="health")
router.register(r"snippets", views.SnippetViewSet)
router.register(r"users", views.UserViewSet)

urlpatterns = router.urls

# Swagger UI URLs
urlpatterns += [
    path(
        "openapi/",
        get_schema_view(
            title="Snippets API",
            description=(
                "Snippets API was built for demo purposes of ScanAPI. "
                "API based on the Django REST Framework's tutorial."
            ),
            version="v1",
            urlconf="snippets.urls",
        ),
        name="openapi-schema",
    ),
    path(
        "swagger-ui/",
        TemplateView.as_view(
            template_name="swagger-ui.html",
            extra_context={"schema_url": "openapi-schema", "version": "v1"},
        ),
        name="swagger-ui",
    ),
]

# Authentication URLs
urlpatterns += [
    path("api-token-auth/", obtain_auth_token, name="api_token_auth"),
    path("rest-auth/registration/", include("rest_auth.registration.urls")),
]
