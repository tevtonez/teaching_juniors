from django.shortcuts import get_object_or_404, render, redirect

from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404

from django.template import loader

from django.core.urlresolvers import reverse_lazy
from django.urls import reverse

from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from django.contrib.auth.decorators import login_required

from django.utils import timezone


from . import forms
from . import models


class SignUpView(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'polls/signup.html'

class MainIndexView(TemplateView):
    template_name = "index.html"

class PollsIndexView(ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return models.Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

class QuestionDetailView(DetailView):
    model = models.Question
    template_name = "polls/detail.html"


class QuestionResultsView(DetailView):
    model = models.Question
    template_name = "polls/results.html"


def vote(request, question_id):
    question = get_object_or_404(models.Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, models.Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question':question,
            'error_message': "You didn't select a choice",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

    return HttpResponse("This is view for voting for a question %s" % question_id)

