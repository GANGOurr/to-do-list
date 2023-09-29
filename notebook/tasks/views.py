from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseNotFound


from .models import Tasks


def index(request):
    list_of_tasks = Tasks.objects.all()
    return render(request, 'tasks/main_tasks.html', context={"title": "Tasks", "list_of_tasks": list_of_tasks})

def edit_my_model(request, pk):
    task = get_object_or_404(Tasks, pk=pk)

    if request.method == 'POST':
        task.title = request.POST['title']
        task.description = request.POST['description']
        task.save()
        return redirect('tasks_list')

    return render(request, 'main_tasks.html', {'task': task})

def create_my_model(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        Tasks.create(title, description)
        return redirect('tasks_list')
    return render(request, 'main_tasks.html')

def delete_my_model(request, pk):
    task = get_object_or_404(Tasks, pk=pk)

    if request.method == 'POST':
        Tasks.delete_by_id(pk)
        return redirect('tasks_list')

    return render(request, 'main_tasks.html', {'task': task})

def show_task(request, task_id):
    t_object = Tasks.get_by_id(task_id)
    return render(request, "tasks/task.html", context={"task_id": task_id, "object": t_object})

def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Page not found</h1>")
