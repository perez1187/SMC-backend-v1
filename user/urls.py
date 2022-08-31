from django.urls import path

from . import views

# api/
urlpatterns = [
    path('register/', views.register_api, name="Register")
]