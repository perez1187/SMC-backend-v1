# from django
from django.urls import path

# from local
from . import views

# from 3rd parties
from knox import views as knox_views

# testing new solution
from rest_framework import routers
from django.conf.urls import include





# old and working ''''

#api/
urlpatterns = [
    path('register/', views.register_api, name="Register"),
    path('login/', views.login_api),
    path('user/', views.get_user_data),
    path('logout/', knox_views.LogoutView.as_view()),
    path('logoutall/', knox_views.LogoutAllView.as_view()),
    # path('email-verify/<token>', views.VerifyEmail.as_view(), name="email-verify"),
]