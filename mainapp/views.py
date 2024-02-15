from django.shortcuts import redirect
from django.shortcuts import render
from django.http import JsonResponse
from .models import TodoModel

def mainpage(request):
    tasks = TodoModel.objects.all()
    return render(request, "mainapp/index.html", {'tasks': tasks})


def add(request):
    task_title = request.POST.get('task-text-input', False)
    if task_title:
        TodoModel(title=task_title).save()
    return redirect("/todo/")
        
    
def update(request, id):
    checkbox_answer = {"on": True, "off": False}
    isComplete_checkbox = request.POST.get('isCompleted', None)
    update_checkbox = TodoModel.objects.get(pk=id)
    if not isComplete_checkbox is None:
        TodoModel.objects.filter(pk=id).update(
            isCompleted=checkbox_answer[isComplete_checkbox]
            )
    return redirect("/todo/")

def delete(request, id):
    TodoModel.objects.get(pk=id).delete()
    return redirect("/todo/")