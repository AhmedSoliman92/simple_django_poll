from django.core.checks import messages
from django.http.response import HttpResponse
from poll.models import Polls
from poll.forms import PollsForm
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.urls import reverse
# Create your views here.


def home(request):
    polls = Polls.objects.all()
    context = {
        'polls': polls
    }
    return render(request, 'home.html', context)


def create(request):
    form = PollsForm()
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = PollsForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['poll_title']
            op1 = form.cleaned_data['option1']
            op2 = form.cleaned_data['option2']
            op3 = form.cleaned_data['option3']
            op4 = form.cleaned_data['option4']
            op5 = form.cleaned_data['option5']

            poll = Polls()
            poll.poll_title = title
            poll.option1 = op1
            poll.option2 = op2
            poll.option3 = op3
            poll.option5 = op5
            poll.option4 = op4
            poll.save()
            messages.add_message(request, messages.SUCCESS,
                                 'You added the poll successfully.')
            return redirect(reverse('home'))
    return render(request, 'create.html', context)


def results(request, id):
    poll = Polls.objects.get(pk=id)

    total = poll.c_option1 + poll.c_option2 + \
        poll.c_option3+poll.c_option4+poll.c_option5
    if total > 0:
        per1 = (poll.c_option1/total)*100
        per2 = (poll.c_option2/total)*100
        per3 = (poll.c_option3/total)*100
        per4 = (poll.c_option4/total)*100
        per5 = (poll.c_option5/total)*100

        context = {'poll': poll, 'total': total, 'per1': per1,
                   'per2': per2, 'per3': per3, 'per4': per4, 'per5': per5}
        return render(request, 'results.html', context)


def vote(request, id):
    poll = Polls.objects.get(pk=id)

    if request.method == 'POST':
        if request.POST['poll'] == 'option1':
            poll.c_option1 += 1
        elif request.POST['poll'] == 'option2':
            poll.c_option2 += 1
        elif request.POST['poll'] == 'option3':
            poll.c_option3 += 1
        elif request.POST['poll'] == 'option4':
            poll.c_option4 += 1
        elif request.POST['poll'] == 'option5':
            poll.c_option5 += 1
        else:
            return HttpResponse(400, 'Invalid form')
        poll.save()
        return redirect(reverse('home'))
    context = {
        'poll': poll
    }

    return render(request, 'vote.html', context)
