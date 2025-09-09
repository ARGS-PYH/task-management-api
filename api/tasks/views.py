from rest_framework import generics, permissions, status, filters
from django.contrib.auth.models import User
from .serializers import UserSerializer
from .models import Task
from .serializers import TaskSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils.timezone import now
from django_filters.rest_framework import DjangoFilterBackend


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny] 


class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ["status", "priority", "due_date"]   
    ordering_fields = ["due_date", "priority"]              

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
    
class TaskCompleteView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, pk):
        try:
            task = Task.objects.get(pk=pk, user=request.user)
            task.status = "Completed"
            task.completed_at = now()
            task.save()
            return Response({"message": "Task marked as complete"}, status=status.HTTP_200_OK)
        except Task.DoesNotExist:
            return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)
        
class TaskIncompleteView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, pk):
        try:
            task = Task.objects.get(pk=pk, user=request.user)
            task.status = "Pending"
            task.completed_at = None
            task.save()
            return Response({"message": "Task reverted to incomplete"}, status=status.HTTP_200_OK)
        except Task.DoesNotExist:
            return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)