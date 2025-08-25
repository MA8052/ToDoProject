from django import forms

class ToDoForm(forms.Form):
    Task1=forms.CharField(required=True,widget=forms.TextInput(attrs={'placeholder': "Try typing 'Buy milk'", 'class': "text-gray-900 text-lg rounded-sm  block w-full pl-3 pr-3 dark:bg-gray-700  dark:placeholder-gray-400 dark:text-white  focus:outline-none not-focus:text-transparent ",'title':'Click to start adding a task'}))