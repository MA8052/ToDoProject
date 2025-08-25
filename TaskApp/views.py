from django.shortcuts import render,get_object_or_404,redirect

from .forms import ToDoForm
from .models import ToDoTable

# Create your views here.



def TaskList(request):
    request.session['check_edit']='Save'
    taskList=ToDoTable.objects.all()
    form=ToDoForm()
    return render(request,'index.html',{'form':form,'taskList':taskList})

def AddTask(request):
        
        if request.session['check_edit']=='Save':
            if request.method=="POST":
                form=ToDoForm(request.POST)
                if form.is_valid():
                    new_Task=request.POST['Task1']
                    SaveRecord=ToDoTable(Task_column=new_Task)
                    SaveRecord.save()
                    message='Saved Successfully!'
        else:
            if request.method=="POST":
                form=ToDoForm(request.POST)
                if form.is_valid():
                    new_Task=request.POST['Task1']
                    task=get_object_or_404(ToDoTable,id=request.session['task_id'])
                    task.Task_column=new_Task
                    task.save()
                    message='Update Successfully!'

        return redirect('TaskList')
        


def TaskEdit(request,task_id):
    
    task=ToDoTable.objects.get(id=task_id)
    form=ToDoForm(initial={'Task1':task.Task_column})
    request.session['check_edit']='Edit'
    request.session['task_id']=task_id
    return render(request,'index.html',{'form':form,'taskList':ToDoTable.objects.all()})

def TaskDelete(request,task_id):
    task=get_object_or_404(ToDoTable,id=task_id)
    task.delete()
    message='Deleted Successfully!'
    return redirect('TaskList')





