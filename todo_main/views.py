from django.shortcuts import render
from todo.models import Task
def home(request):
    incomplete_tasks = Task.objects.filter(is_completed = False).order_by('-updated_at')
    complete_tasks = Task.objects.filter(is_completed = True)
    context ={'incomplete_tasks':incomplete_tasks,
                'complete_tasks':complete_tasks}
    return render(request, 'home.html', context)