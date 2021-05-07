from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
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

urlpatterns = [
    path(
        "openapi",
        get_schema_view(
            title="Snippets API",
            description=(
                "Snippets API was built for demo purposes of ScanAPI. "
                "API based on the Django REST Framework's tutorial."
            ),
            version="1.0.0",
        ),
        name="openapi-schema",
    ),
    path(
        "swagger-ui/",
        TemplateView.as_view(
            template_name="swagger-ui.html",
            extra_context={"schema_url": "openapi-schema"},
        ),
        name="swagger-ui",
    ),
]

urlpatterns += router.urls
