from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.generics import (
    RetrieveUpdateAPIView,
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView
)
from rest_framework.permissions import (
    AllowAny,
    IsAdminUser,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly
)
from .permissions import IsOwnerOrReadOnly
from .models import Todo
from .serializers import (
    RegisterSerializer,
    TodoCreateSerializer,
    TodoListSerializer,
    TodoDetailSerializer
    )
# Create your views here.

class Register(CreateAPIView):
    serializer_class = RegisterSerializer

    # permission_classes = [IsAuthenticated.__invert__()]
    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.create_user(username, email, password)
        user.save()
        return Response({'detail': 'User has been create'})

class TodoCreateApiView(CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoCreateSerializer
    # permission_classes = [IsAdminUser, IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TodoDeleteApiView(DestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoDetailSerializer
    # permission_classes = [IsAdminUser, IsOwnerOrReadOnly]
    lookup_field = 'slug'

class TodoUpdateApiView(RetrieveUpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoDetailSerializer
    # permission_classes = [IsAdminUser, IsOwnerOrReadOnly]
    lookup_field = 'slug'

class TodoDetailApiView(RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoDetailSerializer
    lookup_field = 'slug'
    # permission_classes = [IsAuthenticatedOrReadOnly]

class TodoListApiView(ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoListSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]
