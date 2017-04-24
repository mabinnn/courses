from django.shortcuts import render, redirect
from .models import Course

def index(request):
    print "I AM THE INDEX def", request
    context = {
        "courses" : Course.objects.all()
    }
    print Course.objects.all()
    return render(request, "courses_app/index.html", context)

def add(request):
    Course.objects.create(course_name=request.POST['course_name'], description=request.POST['description'])
    print "I AM THE ADD def", request
    return redirect('/')

def confirm(request, id):
    print "THIS IS THE CONFIRMATION DEF", request
    context = {
        "courses" : Course.objects.filter(id=id)
    }
    return render(request, "courses_app/confirmation_page.html", context)

def delete(request, id):
    print "THIS IS THE DELETE DEF"
    Course.objects.filter(id=id).delete()
    return redirect('/')
