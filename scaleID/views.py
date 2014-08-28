from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext, loader

# Create your views here.
def scaleID(request):
    return render_to_response("scaleID.html", {}, context_instance=RequestContext(request))


def post_data(request):
    if request.is_ajax():
        message = "Yes, AJAX!"
    else:
        message = "Not Ajax"
    return HttpResponse(message)
