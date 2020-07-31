from django.urls import path, include
from .views import registrationView

urlpatterns = [path("registration/", registrationView, name="registration_view")]
