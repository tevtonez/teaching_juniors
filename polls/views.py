from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse

from django.core.urlresolvers import reverse_lazy
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from django.contrib.auth.decorators import login_required

from . import forms
from . import models

class SignUpView(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'polls/signup.html'


class IndexView(TemplateView):
    template_name = 'index.html'


class pollsIndexView(TemplateView):
    template_name = 'polls/base.html'


def index(request):
    return HttpResponse("hi there")

