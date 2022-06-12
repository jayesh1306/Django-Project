from django.http import HttpResponse
from .models import Topic, Course, Student, Order
from django.shortcuts import get_object_or_404

#  Import render for rendering templates
from django.shortcuts import render


def index(request):
    # Part B answer
    top_list = Topic.objects.all().order_by('id')[:10]
    return render(request, 'mywebapp/index0.html', {'top_list': top_list})

#  Part C answer
# We are passing top_list to template because we have to access it to the template file which we will create so that this data can be accessed in that template.


def about(request):
    print("Welcome guys")
    return render(request, 'mywebapp/about0.html')


def detail(request, top_no):
    response = HttpResponse()
    topics = Topic.objects.filter(id=top_no).values()
    if not topics:
        response.write(get_object_or_404(topics))
        return response

    # para = '<p> Category is:  ' + str(topics[0].get('category')) + '</p>'
    # response.write(para)
    courses = Course.objects.filter(topic=top_no)

    # response.write('<ul>')
    # for c in courses:
    #     para = '<li>' + str(c) + '</li>'
    #     response.write(para)
    # response.write('</ul>')
    return render(request, 'mywebapp/detail0.html', {'topic_name': topics[0].get('category'),'name' : topics[0].get('name'), 'courses': courses})
