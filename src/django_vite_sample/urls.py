from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter

from django_vite_sample.todos.views import TodoViewSet, todo_delete, todo_done, todo_list

router = DefaultRouter()
router.register("todos", TodoViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    path("", todo_list, name="todo-list"),
    path("<int:pk>/done/", todo_done, name="todo-done"),
    path("<int:pk>/delete/", todo_delete, name="todo-delete"),
    path("about/", TemplateView.as_view(template_name="todos/about.html"), name="about"),
]
