from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse
from .models import TodoModel

def mainpage(request):
    tasks = TodoModel.objects.all()
    data = {}
    s = []
    for task in tasks:
        data = {
            "id": task.pk,
            "title": task.title,
            "isComplete": task.isCompleted,
            "create_date": task.add_date
        }
        s.append(data)
    
    print(s)
    return JsonResponse(data)

