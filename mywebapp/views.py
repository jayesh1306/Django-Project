from django.http import HttpResponse
from .models import Topic, Course, Student, Order
from django.shortcuts import  get_object_or_404


def index(request):
    course_list = Course.objects.all().order_by('-price')[:10]
    response = HttpResponse()
    heading1 = '<p>' + 'List of Courses: '  + '</p>' 
    response.write(heading1)
    for course in course_list:
        if course.for_everyone == True:
            para = '<p>' + str(course.id) + ': ' + str(course) + ' : <b>This course is for Everyone</b></p>'
        else:
            para = '<p>' + str(course.id) + ': ' + str(course) + ' : <b>This course is not for Everyone</b></p>'    
        response.write(para)
    return response

def about(request):
    response = HttpResponse()
    response.write("This is an E-learning Website! Search our Topics to find all available Courses.")
    return response

def detail(request, top_no):
    topic_detail = Topic.objects.filter(id=top_no).values()
    if not topic_detail:
        datatoSend = get_object_or_404(topic_detail)
    else:
        response = HttpResponse()
        para = '<p>Detail for Topic <br>ID: ' + str(topic_detail[0].get('id')) + '<br> Name: <b>' + str(topic_detail[0].get('name')) + '</b><br>Category: <b>' + str(topic_detail[0].get('category')) +'</b></p>'
        course_list = Course.objects.filter(topic=topic_detail[0].get('id'))
        print(course_list)
        headingForTitle = '<p>List of course for that topic are as below</p>'
        dataToSend = para + headingForTitle
        for course in course_list:
            print(course)
            dataToSend += '<li>' + str(course) + '</li>'
    response.write(dataToSend)
    return response