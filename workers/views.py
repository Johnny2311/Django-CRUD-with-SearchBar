from django.shortcuts import render, redirect
from workers.models import Worker
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .forms import WorkerForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import datetime


def index(request):
    return redirect(reverse_lazy('worker_list'))

class WorkersList(ListView):
    context_object_name = 'workers'    
    paginate_by = 3

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context (the workers)
        context = super().get_context_data(**kwargs)  
        # Adding another keys to show in the template
        context['q'] = self.request.GET.get('q', '')
        context['field'] = self.request.GET.get('field', '')
        return context

    def get_queryset(self):
        q = self.request.GET.get('q', '')
        field = self.request.GET.get('field', '')
        workers = Worker.objects.all()
        if q and field:
            if field == "name":
                workers = Worker.objects.filter(name__icontains=q)
            elif field == "age":
                elapsed = timezone.now() - datetime.timedelta(days=int(q) * 365)
                workers = Worker.objects.filter(Q(birthdate__lt=elapsed) & Q(birthdate__gt=elapsed - datetime.timedelta(days=365)))
            elif field == "deparment":    
                workers = Worker.objects.filter(deparment__icontains=q)
        return workers

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
    

# Function-Based-View for list, search and paginate

# def worker_list(request):
#     q = request.GET.get('q', '')
#     field = request.GET.get('field', '')
#     workers = Worker.objects.all()
#     if q and field:
#         if field == "name":
#             workers = Worker.objects.filter(name__icontains=q)
#         elif field == "age":
#             elapsed = timezone.now() - datetime.timedelta(days=int(q) * 365)
#             workers = Worker.objects.filter(Q(birthdate__lt=elapsed) & Q(birthdate__gt=elapsed - datetime.timedelta(days=365)))
#         elif field == "deparment":    
#             workers = Worker.objects.filter(deparment__icontains=q)

#     page = request.GET.get('page', 1)
#     paginator = Paginator(workers, 3)

#     try:
#         workers = paginator.page(page)
#     except PageNotAnInteger:
#         workers = paginator.page(1)
#     except EmptyPage:
#         workers = paginator.page(paginator.num_pages)

#     return render(request, 'workers/worker_list.html', {'workers': workers, 'q': q, 'field': field})