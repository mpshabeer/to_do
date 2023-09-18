from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
# Create your views here.
from todoapp.models import Task

class TaskListView(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'details'

class DetailListView(DetailView):
    model = Task
    template_name = 'details.html'
    context_object_name = 'details'


class DeleteView(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('listview')



class TaskUpdate(UpdateView):
    model=Task
    template_name='update.html'
    context_object_name='task'
    fields=('task','priority','date')
    def get_success_url(self):
        return reverse_lazy('detail',kwargs={'pk':self.object.id})
from .forms import *
def index(request):
    details = Task.objects.all()
    if request.method=="POST":
        task=request.POST.get('task')
        priority=request.POST.get('priority')
        date=request.POST.get('date')
        task=Task(task=task,priority=priority,date=date)
        task.save()
        return redirect("/")
    return render(request,"home.html",{'details':details})



def delete(request,id):
    if request.method=='POST':
        task=Task.objects.get(id=id)
        task.delete()
        return redirect('/')
    return render(request,"delete.html")

def detail(request):
    details=Task.objects.all()

    return render(request,"details.html",{'details':details})

def update(request,id):
    task=Task.objects.get(id=id)
    f=TodoForm(request.POST or None,instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,"edit.html",{'f':f,'task':task})



