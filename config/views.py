from braces.views import LoginRequiredMixin
from django.views.generic import TemplateView


class ConfigTemplateView(LoginRequiredMixin, TemplateView):

    template_name = 'pages/home.html'
