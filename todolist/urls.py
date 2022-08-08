from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('del/<int:todo_id>', views.delete),
    path('add/', views.add),
    path('complete/<int:todo_id>', views.complete),
    path('cancel/<int:todo_id>', views.cancel),
]
