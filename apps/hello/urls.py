from django.urls import path
from hello.views import AboutView

app_name = "hello"
urlpatterns = [
    path("about/", AboutView.as_view(), name="about"),
]
