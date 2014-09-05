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

    the_visit = Visit.objects.get(pk=visit_id)
    print "got the visit"


    if request.is_ajax():
        message = "Yes, AJAX!"
    else:
        message = "Not Ajax"

    print("received Ajax request")

    age =  request.POST[u'age']
    handedness = request.POST[u'handedness']
    nationality = request.POST[u'nationality']
    lessons = request.POST[u'lessons']
    sing = request.POST[u'sing']
    email = request.POST[u'email']

    print "got the age: " + str(age)


    the_visit.age = age

    the_visit.handed = handedness
    print "got handedness: " + handedness

    the_visit.nationality = nationality
    print "got nationality: " + nationality

    the_visit.lessons = (lessons == "true")
    print "got lessons: " + str(lessons)

    the_visit.sing = (sing == "true")
    print "got sing true/false: " + str(sing)

    the_visit.email = email
    print "got email: " + email

    print "set the age"

    the_visit.save()

    print "saved the visit"

    return HttpResponse(message)


def post_comparison(request):

    print "post comparison API has been called"
    print "post data below:"
    print request.POST


    if request.is_ajax():
        message = "Yes, AJAX!"
    else:
        message = "Not Ajax"


    visit_id = request.session["visit_id"]

    the_visit = Visit.objects.get(pk=visit_id)
    print "got the visit"


    left_scale = request.POST[u'leftScale']
    print "left_scale: " + str(left_scale)

    center_scale = request.POST[u'centerScale']
    right_scale = request.POST[u'rightScale']
    right_direction = request.POST[u'rightDirection']

    answer_correct = (request.POST[u'answerCorrect'] == "true")
    print "answerCorrect: " + str(answer_correct)

    time_spent = request.POST[u'timeSpent']
    interval = request.POST[u'interval']
    just_intonation = (request.POST[u'justIntonation'] == "true")
    mode = request.POST[u'mode']
    clicks_left = request.POST[u'clicksLeft']
    clicks_center = request.POST[u'clicksCenter']
    clicks_right = request.POST[u'clicksRight']

    print "collected all data"


    new_comparison = Comparison(visit=the_visit, left_scale=left_scale, center_scale=center_scale, right_scale=right_scale,
        right_direction=right_direction, answer_correct=answer_correct, time_spent=time_spent, speed_interval=interval,
        just_intonation=just_intonation, mode=mode, clicks_left=clicks_left, clicks_center=clicks_center, clicks_right=clicks_right)

    print "made the new comparison"

    new_comparison.save()

    print "saved the comparison"





    return HttpResponse(message)




def report_panel(request):

    visits = Visit.objects.all()
    comparisons = Comparison.objects.all()

    num_visits = len(visits)
    num_complete_visits = 0
    num_comparisons = len(comparisons)
    num_emails = 0
    guesses_left = 0
    guesses_right = 0

    left_correct = 0
    left_total = 0

    right_correct = 0
    right_total = 0

    sing_total = 0
    not_sing_total = 0
    sing_correct = 0
    not_sing_correct = 0

    lessons_correct = 0
    lessons_total = 0
    no_lessons_correct = 0
    no_lessons_total = 0

    total_complete_correct_comparisons = 0

    visits_correct_count = [0,0,0,0,0,0,0,0,0,0,0]

    scale_comparisons = {}

    for visit in visits:
        local_correct_count = 0

        if len(visit.comparisons.all()) == 10:
            complete_visit = True

            num_complete_visits += 1
            if visit.email != "":
                num_emails += 1

            for comparison in visit.comparisons.all():
                if comparison.answer_correct == True:
                    local_correct_count += 1
                    total_complete_correct_comparisons += 1


                if guess_right(comparison):
                    guesses_right += 1
                else:
                    guesses_left += 1



                if visit.sing:
                    sing_total += 1
                    if comparison.answer_correct:
                        sing_correct += 1
                else:
                    not_sing_total += 1
                    if comparison.answer_correct:
                        not_sing_correct += 1

                if visit.lessons:
                    lessons_total += 1
                    if comparison.answer_correct:
                        lessons_correct += 1
                else:
                    no_lessons_total += 1
                    if comparison.answer_correct:
                        no_lessons_correct += 1



                if visit.handed == "left":
                    left_total += 1
                    if comparison.answer_correct==True:
                        left_correct += 1
                else:
                    right_total += 1
                    if comparison.answer_correct==True:
                        right_correct += 1



            visits_correct_count[local_correct_count] += 1


        else:
            complete_visit = False


    left_percent = (left_correct + 0.0) / left_total
    right_percent = (right_correct + 0.0) / right_total

    sing_percent = (sing_correct + 0.0) / sing_total
    not_sing_percent = (not_sing_correct + 0.0) / not_sing_total

    lessons_percent = (lessons_correct + 0.0) / lessons_total
    no_lessons_percent = (no_lessons_correct + 0.0 ) / lessons_total

    num_complete_comparisons = num_complete_visits * 10
    comparisons_percent = (total_complete_correct_comparisons + 0.0) / num_complete_comparisons

    return render_to_response('report.html', {"num_visits": num_visits, "num_complete_visits": num_complete_visits,
        "num_comparisons": num_comparisons, "num_complete_comparisons": num_complete_comparisons,
        "num_emails": num_emails, "visits_correct_count": visits_correct_count, "guesses_left": guesses_left, "guesses_right": guesses_right,
        "left_percent": left_percent, "right_percent": right_percent, "comparisons_percent": comparisons_percent,
        "sing_percent": sing_percent, "not_sing_percent": not_sing_percent, "lessons_percent": lessons_percent,
        "no_lessons_percent": no_lessons_percent,

        }, context_instance=RequestContext(request) )


def guess_right(comparison):
    if comparison.center_scale == comparison.right_scale:
        guess_right = True
    else:
        guess_right = False

    if comparison.answer_correct:
        return guess_right
    else:
        return not guess_right



