from django.shortcuts import render
from rest_framework import generics
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Scrip
from .serializers import ScripSerializer


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

# class ListScripView(generics.ListAPIView):
#     """
#     Provides a get method handler.
#     """
#     queryset = Scrip.objects.all()
#     serializer_class = ScripSerializer

@csrf_exempt
def scrip_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        scrips = Scrip.objects.all()
        serializer = ScripSerializer(scrips, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ScripSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
            
@csrf_exempt
def scrip_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        scrip = Scrip.objects.get(pk=pk)
    except Scrip.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ScripSerializer(scrip)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ScripSerializer(scrip, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        scrip.delete()
        return HttpResponse(status=204)