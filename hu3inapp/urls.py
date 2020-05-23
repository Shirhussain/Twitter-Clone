from django.urls import path
from . views import home

app_name = "hu3inapp"
urlpatterns = [
    path("", home, name = "home")
]