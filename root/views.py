from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from task.models import Task
from task.forms import TaskForm,TaskUpdateForm
from django.contrib import messages
import json
from datetime import datetime
from django.contrib.auth.decorators import login_required
def index(request):
    return render(request,'task.html')

@csrf_exempt
def task(request):
    tasks = Task.objects.all()
    if request.method == 'POST':
        start = request.POST.get('start')
        end = request.POST.get('end')
        month = datetime.now().month
        if start and end:
            result = Task.objects.filter(start_date__gte=start, end_date__lte=end).values()
        elif start:
            result = Task.objects.filter(start_date=start).values()
        elif end:
            result = Task.objects.filter(end_date=end).values()
        else:
            result = Task.objects.filter(start_date__month__gte=month).values()
        return JsonResponse({"tasks": list(result)})
        return HttpResponse(json.dumps(data), content_type="application/json")
    return render(request,'task.html')

def add_task(request):
    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task Added')
    return render(request,'add_task.html',{'form':form})

def update(request,id):
    task = get_object_or_404(Task, pk=id)
    form = TaskUpdateForm(instance=task)
    if request.method == "POST":
        form = TaskUpdateForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task Updated')
    return render(request,'task-update.html',{'form':form})

def delete(request,id):
    task = get_object_or_404(Task, pk=id).delete()
    messages.success(request, 'Task Deleted')
    try:
        return redirect(request.META.get('HTTP_REFERER'))
    except:
        return redirect('/')