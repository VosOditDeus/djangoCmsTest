from django.http import JsonResponse
from django.shortcuts import render
import json
# Create your views here.



def saveGrid(request):
    data = request.GET
    print(request.GET)
    with open('Grid.json', 'w') as outfile:
        json.dump(data, outfile)
        return JsonResponse({'result': True})