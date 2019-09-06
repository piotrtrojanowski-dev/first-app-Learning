from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy


from .models import Topic, Entry
from .forms import TopicForm, EntryForm


def index(request):
    """Home for Learning log app."""
    return render(request,'learning_log/index.html')

@login_required
def topics(request):
    """Page with all topics"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_add')
    context = {'topics':topics}
    return render(request,"learning_log/topics.html", context)

@login_required
def topic(request, pk):
    """Page with single topic. """
    topic = Topic.objects.get(pk=pk)
    #Upewniamy sie, ze temat nalezy do biezacego uzytkownika
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by('-date_add')
    context = {"topic":topic, "entries":entries}
    return render(request, 'learning_log/topic.html', context)

@login_required
def new_topic(request):
    """Page to create new topic."""
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            form.save()
            return redirect('topics')

    return render(request, 'learning_log/new_topic.html', {'form':form})

@login_required
def new_entry(request,pk):
    """Page to create new entry"""
    topic = Topic.objects.get(pk=pk)

    if request.method != "POST":
        form = EntryForm()
    else:
        form = EntryForm(request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect("topic", pk=topic.pk)

    return render(request, "learning_log/new_entry.html", {'form':form, 'topic':topic})

@login_required
def edit_entry(request, pk):
    """Page to edit entry"""
    entry = Entry.objects.get(pk=pk)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404
    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("topic", pk=topic.pk)

    return render(request, 'learning_log/edit_entry.html', {"entry":entry, "topic":topic, "form":form})

class EntryDeleteView(DeleteView):
    """Page to delete entry"""
    model = Entry
    success_url = reverse_lazy('topics')


class TopicDeleteView(DeleteView):
    """Page to delete topic"""
    model = Topic
    success_url = reverse_lazy('topics')