
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.urls import reverse
from django.utils.http import urlencode
from webapp.models import Project
from django.views.generic import TemplateView, FormView, ListView
from webapp.forms import SimpleSearchForm


class ProjectIndexView(ListView):
    template_name = 'project/index.html'
    context_object_name = 'projects'
    model = Project
    ordering = ['start_date']

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            query = Q(name__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset

    def get_search_form(self):
        return SimpleSearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None