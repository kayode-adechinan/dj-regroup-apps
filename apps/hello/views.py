# some_app/views.py
from django.views.generic import TemplateView


class AboutView(TemplateView):
    template_name = "hello/about.html"
