from __future__ import unicode_literals

from django.views.generic import TemplateView, ListView, DetailView


class AboutView(TemplateView):
	template_name = 'about.html'


class HomeView(TemplateView):
    template_name = 'index.html'


class WorkList(ListView):
    template_name = 'work.html'


class WorkDetail(DetailView):
    template_name = 'work_detail.html'