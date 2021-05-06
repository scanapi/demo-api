from django.urls import path, include
from rest_framework.routers import DefaultRouter
from snippets import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.get_api_root_view().cls.__name__ = "Demo API"
router.get_api_root_view().cls.__doc__ = (
    "ScanAPI's API built for demo purposes. "
    "API based on the Django REST Framework's tutorial."
)
router.register(r"snippets", views.SnippetViewSet)
router.register(r"users", views.UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path("", include(router.urls)),
]
