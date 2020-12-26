from django.shortcuts import render
from workers.models import Worker
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .forms import WorkerForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.utils import timezone
import datetime

class WorkersList(ListView):
    model = Worker
    context_object_name = 'workers'

class WorkerDetail(DetailView):
    model = Worker
    context_object_name = 'worker'

class WorkerCreate(SuccessMessageMixin, CreateView):
    model = Worker
    form_class = WorkerForm
    success_url = reverse_lazy('worker_list')
    success_message = 'Worker successfully created!'

class WorkerUpdate(SuccessMessageMixin, UpdateView):
    model = Worker
    form_class = WorkerForm
    context_object_name = 'worker'
    success_url = reverse_lazy('worker_list')
    success_message = 'Worker successfully updated!'

class WorkerDelete(SuccessMessageMixin, DeleteView):
    model = Worker
    success_url = reverse_lazy('worker_list')
    success_message = 'Worker successfully deleted!'
    
def worker_search(request):
    q = request.GET['query']
    if request.GET['field'] == "name":
        workers = Worker.objects.filter(name__icontains=q)
    elif request.GET['field'] == "age":
        elapsed = timezone.now() - datetime.timedelta(days=int(q) * 365)
        workers = Worker.objects.filter(Q(birthdate__lt=elapsed) & Q(birthdate__gt=elapsed - datetime.timedelta(days=365)))
    elif request.GET['field'] == "deparment":    
        workers = Worker.objects.filter(deparment__icontains=q)
    path = request.get_full_path()
    if "name" in path:
        field = "name"
    elif "age" in path:
        field = "age"
    elif "deparment" in path:
        field = "deparment"
    return render(request, 'workers/worker_list.html', {'workers': workers, 'q': q, 'field': field})

