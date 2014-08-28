from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext, loader
from scaleID.models import Visit, Comparison


#set id for the whole session
# submit comparisons
# submit survey
# capture each, create database objects



# Create your views here.
def scaleID(request):


    # create the session and save it to the current session
    new_visit = Visit()
    new_visit.save()
    request.session["visit_id"] = new_visit.pk

    print "new_visit id: " + str(new_visit.pk)

    print "confirming that it has been stored in session: " + str(request.session["visit_id"])


    return render_to_response("scaleID.html", {}, context_instance=RequestContext(request))




def post_survey(request):

    print "confirming that visit id has survived in session: " + str(request.session["visit_id"])
    visit_id = request.session["visit_id"]

    if request.is_ajax():
        message = "Yes, AJAX!"
    else:
        message = "Not Ajax"

    print("received Ajax request")

    age =  request.POST[u'age']
    handedness = request.POST[u'handedness']
    nationality = request.POST[u'']
    lessons = request.POST[u'lessons']
    sing = request.POST[u'sing']
    email = request.POST[u'email']

    print "got the age: " + str(age)

    the_visit = Visit.objects.get(pk=visit_id)

    print "got the visit"
    print the_visit

    the_visit.age = age
    the_visit.handedness = handedness
    the_visit.nationality = nationality
    the_visit.lessons = lessons
    the_visit.sing = sing
    the_visit.email = email

    print "set the age"

    the_visit.save()

    print "saved the visit"

    return HttpResponse(message)


def post_comparison(request):

    if request.is_ajax():
        message = "Yes, AJAX!"
    else:
        message = "Not Ajax"

    print request.POST.dict()[u'survey_data[handedness]']


    return HttpResponse(message)


