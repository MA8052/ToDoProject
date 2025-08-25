from django.urls import path
from .import views

#by default
#http://localhost:8000/

#by default
#http://localhost:8000/TaskApp/TaskList

urlpatterns = [
    path('',views.TaskList,name='TaskList'),
    path('AddTask/',views.AddTask,name='AddTask'),
    path('TaskEdit/<int:task_id>/',views.TaskEdit,name='TaskEdit'),
    path('TaskDelete/<int:task_id>/',views.TaskDelete,name='TaskDelete'),
]
