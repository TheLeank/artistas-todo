from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('task/', views.create, name='create_task'),
    path('task/<int:task_id>/', views.handle, name='handle_task'),
    path('tasks/', views.tasks, name='get_tasks'),
]