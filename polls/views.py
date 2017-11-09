from django.shortcuts import get_object_or_404, render, redirect

from django.http import HttpResponse
from django.http import Http404

from django.template import loader

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
    latest_question_list = models.Question.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }

    return render(request,'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(models.Question,pk=question_id)
    return render(request, 'polls/detail.html', {'question':question})

def results(request, question_id):
    response = "This is question's %s results"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("This is view for voting for a question %s" % question_id)
