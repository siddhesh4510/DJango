from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from myapp.models import ToDoList
# Create your views here.
def index(request):
    return render(request, 'index.html')

def search_page(request):
    return render(request, 'search.html')


def add(request):
    print(request.POST["taskname"])
    t=ToDoList(taskname=request.POST["taskname"] , enddate=request.POST["enddate"])
    t.save()
    return HttpResponseRedirect('/table')


    #return HttpResponse("hi")
def changestatus(request , id):
    print(id)
    ToDoList.objects.filter(id=id).update(iscomplete=True)
    return HttpResponseRedirect('/table')

def table(request):
    tasks=ToDoList.objects.all()
    return render(request, 'table.html' ,{'tasks':tasks})

def update(request , id):
    print("hello r")
    t=ToDoList.objects.filter(id=id)
    print("hello r")
    return render(request, 'edit.html' , {'taskname':t[0].taskname , 'enddate':t[0].enddate ,'id':id})

def edit(request , id):
    ToDoList.objects.filter(id=id).update(taskname=request.POST.get('taskname'),enddate=request.POST.get('enddate'))
    return HttpResponseRedirect('/table')

def delete(request , id):
    ToDoList.objects.filter(id=id).delete()
    return HttpResponseRedirect('/table')

def search(request ):
    print("In Search")
    t=ToDoList.objects.filter(taskname__contains=request.POST.get('taskname'))
    return render(request, 'search.html' ,{'tasks':t ,'searched_data':True})





