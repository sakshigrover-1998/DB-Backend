from django.shortcuts import render
from Users.models import UserData
from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from Users.models import UserData
from Users.serializers import UserDataSerializer

# Create your views here.
# Create your views here.




@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'getUserRecords': '/getUserRecords/',
       
    }

    return Response(api_urls)


@api_view(['GET'])
def getUserRecords(request):
    records = UserData.objects.all()
    serializer = UserDataSerializer(records, many=True)
    return Response(serializer.data)
