from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView


class HomeView(TemplateView):

    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
