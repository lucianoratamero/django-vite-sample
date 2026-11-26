from django import forms
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from rest_framework import serializers, viewsets

from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ["id", "text", "done"]


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


# Server-rendered pages: the same todos, managed with plain HTML forms instead of the JSON API.
class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["text"]
        widgets = {"text": forms.TextInput(attrs={"placeholder": "What needs doing?"})}


def todo_list(request):
    form = TodoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("todo-list")
    todos = Todo.objects.all()
    remaining = Todo.objects.filter(done=False).count()
    return render(
        request, "todos/todo_list.html", {"todos": todos, "remaining": remaining, "form": form}
    )


@require_POST
def todo_done(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.done = request.POST.get("done") == "true"
    todo.save()
    return redirect("todo-list")


@require_POST
def todo_delete(request, pk):
    get_object_or_404(Todo, pk=pk).delete()
    return redirect("todo-list")
