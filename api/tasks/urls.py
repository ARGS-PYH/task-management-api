from django.urls import path
from .views import (
    UserCreateView, UserListView, UserDetailView,
    TaskListCreateView, TaskDetailView,
    TaskCompleteView, TaskIncompleteView
)

urlpatterns = [
    path("users/", UserListView.as_view(), name="user-list"),
    path("users/create/", UserCreateView.as_view(), name="user-create"),
    path("users/<int:pk>/", UserDetailView.as_view(), name="user-detail"),

    path("tasks/", TaskListCreateView.as_view(), name="task-list-create"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("tasks/<int:pk>/complete/", TaskCompleteView.as_view(), name="task-complete"),
    path("tasks/<int:pk>/incomplete/", TaskIncompleteView.as_view(), name="task-incomplete"),
]
