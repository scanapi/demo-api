"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from demo.api import views

urlpatterns = [
    path("api/health", views.health, name="api-health"),
    path("api/devs/", views.dev_list, name="api-dev-list"),
    path("api/devs/<uuid:identifier>", views.dev_details, name="api-dev-details"),
    path(
        "api/devs/<uuid:identifier>/languages",
        views.dev_details_languages,
        name="api-dev-details-languages",
    ),
    path("api/languages/", views.language_list, name="api-language-list"),
]
