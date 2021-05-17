from django.urls import path

from api import views

urlpatterns = [
    path("", views.root, name="api-root"),
    path("health/", views.health, name="api-health"),
    path("devs/", views.dev_list, name="api-dev-list"),
    path("devs/<uuid:identifier>", views.dev_details, name="api-dev-details"),
    path(
        "devs/<uuid:identifier>/languages",
        views.dev_details_languages,
        name="api-dev-details-languages",
    ),
    path("languages/", views.language_list, name="api-language-list"),
]
