from django.shortcuts import render

from django.views.generic import TemplateView

from apps.web.models import Site


class HomeView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        site = Site.objects.first()
        context['site'] = site
        return context