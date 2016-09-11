from __future__ import unicode_literals

from django.views.generic import TemplateView, ListView, DetailView

from .models import Project


class AboutView(TemplateView):
	template_name = 'bio.html'


class HomeView(ListView):
	template_name = 'index.html'
	model = Project

	def get_context_data(self, **kwargs):
		context = super(HomeView, self).get_context_data(**kwargs)
		context['project_list'] = Project.objects.filter(
			featured=True).order_by('order')
		return context


class WorkList(ListView):
	model = Project
	template_name = 'work.html'
	ordering = ('order')


class WorkDetail(DetailView):
	model = Project
	template_name = 'work_detail.html'

	def get_context_data(self, **kwargs):
		context = super(WorkDetail, self).get_context_data(**kwargs)
		context['tags'] = Project.objects.filter(tags=True)
		context['happy_chat'] = ['Building', 'Creating', 'The Making of', 'About']
		return context