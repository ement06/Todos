from django.urls import path, include

from .views import (
    TodoListApiView,
    TodoDetailApiView,
    TodoUpdateApiView,
    TodoDeleteApiView,
    TodoCreateApiView,
    Register,
)
urlpatterns = [
    path('user/singup/', Register.as_view(), name='registration'),
    path('user/', include('rest_auth.urls')),
    path('todos/', TodoListApiView.as_view(), name = 'todo-list'),
    path('todos/create', TodoCreateApiView.as_view(), name='todo-create'),
    path('todos/<str:slug>', TodoDetailApiView.as_view(), name='todo-detail'),
    path('todos/<str:slug>/delete', TodoDeleteApiView.as_view(), name='todo-delete'),
    path('todos/<str:slug>/edit', TodoUpdateApiView.as_view(), name='todo-update'),

]
