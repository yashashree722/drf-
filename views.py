from django.shortcuts import render
import io
from rest_framework .parsers import JSONParser
from .serializers import StudentSerializers
from rest_framework .renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def studentcreate(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializers = StudentSerializers(data = python_data)
        if serializers.is_valid():
            serializers.save()
            msz = {'msz': 'data created'}
            json_data = JSONRenderer().render(msz)
            return HttpResponse(json_data,content_type = 'application/json')
        
    json_data = JSONRenderer().render(serializers._errors)
    return HttpResponse(json_data,content_type = 'application/json')


