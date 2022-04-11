from django.shortcuts import render
from django.db.models.query import QuerySet
from rest_framework import viewsets
from task_management_app.serializers import TaskSerializers
from task_management_app.models import Task


# Create your views here.
class TaskView(viewsets.ModelViewSet):
    serializer_class = TaskSerializers
    queryset = Task.objects.all()
