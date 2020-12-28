from django.core.serializers import serialize
from django.http import HttpResponse, JsonResponse, QueryDict
from django.views.decorators.csrf import csrf_exempt

from .models import Task


@csrf_exempt
def create(request):
    """
    Creates new Task()
    """
    if request.method == 'POST':
        task = Task()
        task.text = request.POST.get('text', 'null')
        task.status = request.POST.get('status', False)
        task.save()
        return HttpResponse(status=201)
    else:
        return HttpResponse(status=400)


@csrf_exempt
def handle(request, task_id):
    """
    handle single task
    """   
    # Read
    if request.method == 'GET':
        task = Task.objects.get(id=task_id)
        output = {
            'id':task.id,
            'text':task.text,
            'status':task.status
        }   
        return JsonResponse(output)

    # Update
    elif request.method == 'PUT':
        put_dict = {k: v[0] if len(v)==1 else v for k, v in QueryDict(request.body).lists()}
        task = Task.objects.get(id=task_id)
        task.text = put_dict['text']
        task.status = put_dict['status']
        task.save()
        output = {
            'id':task.id,
            'text':task.text,
            'status':task.status
        }
        return JsonResponse(output)
        
    # Delete
    elif request.method == 'DELETE':
        task = Task.objects.get(id=task_id)
        task.delete()
        return HttpResponse(status=204)
    else:
        return HttpResponse(status=400)


        
@csrf_exempt
def tasks(request):
    """
    return all tasks
    """
    tasks = Task.objects.all()
    task_list = {}
    for task in tasks:
        entry = {'text':task.text, 'status':task.status}
        task_list[task.id] = entry
    return JsonResponse(task_list)