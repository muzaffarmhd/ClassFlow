from django.urls import path
from .views import SignUpView

app_name="finewell"

urlpatterns = [
    path("signup/", SignUpView.as_view(), name='signup')
]
