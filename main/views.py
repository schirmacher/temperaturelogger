from datetime import datetime
import json

from django.views.decorators.csrf import csrf_exempt

from .models import Temperature

from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.utils import timezone
from main.forms import TemperatureForm


# Create your views here.
#def index(request):
#    return render(request, "index.html")

def index(request):
    return HttpResponse("Hello.")


def db(request):
    # Query all Temperature objects
    temperatures = Temperature.objects.all()

    # Serialize the queryset to JSON
    data = serializers.serialize('json', temperatures)

    # Return the serialized data in a JsonResponse
    return JsonResponse(data, safe=False)


@csrf_exempt
def dbwrite(request):

    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = TemperatureForm(request.POST)

        # Check if the form is valid:
        flag = form.is_valid()
        errors = form.errors
        if errors:
            print("form_is_valid: %s" % flag)
            print("errors: %s" % errors)
        if flag:
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            sensor = form.cleaned_data["sensor"]
            value = form.cleaned_data["value"]
            if sensor != "":
                temperature = Temperature()
                temperature.sensor = sensor
                temperature.value = value
                temperature.when = timezone.now()
                temperature.save()

    # If this is a GET (or any other method) do nothing
    return HttpResponseRedirect('/')
