from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="tasks_list"),
    path('task/<int:task_id>/', views.show_task, name="show_task"),
    path('task/<int:pk>/edit/', views.edit_my_model, name='edit_my_task'),
    path('task/create/', views.create_my_model, name='create_new_task'),
    path('task/<int:pk>/delete/', views.delete_my_model, name='delete_task'),
]