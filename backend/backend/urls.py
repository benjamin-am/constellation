"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from django.urls import path
from . import views


urlpatterns = [
    path("api/notes/", views.notes_api, name="notes-api"),
    path("api/notes/<int:note_id>/", views.get_note_by_id, name="get-note-by-id"),
    path(
        "api/notes/allnotes/", views.get_all_notes_preview, name="get-all-notes-preview"
    ),
    path("api/analyze/", views.analyze_note_api, name="analyze-note-api"),
]
