from django.shortcuts import render

# Create your views here.
import json
from django.http import HttpResponse

from django.views.decorators.csrf import  csrf_exempt

def hello(request):
    return HttpResponse("Hello world ! ")

@csrf_exempt
def my_api(request):
    dic = {}
    if request.method == "GET":
        dic['message'] = 0
        return HttpResponse(json.dumps(dic))
    else:
        dic['message'] = 'error method~~'
        return HttpResponse(json.dumps(dic,ensure_ascii=False))

@csrf_exempt
def phoneLocation(request):
    if request.method == "GET":
        dic = {}
        d = {}
        dic['success'] = True
        d['proviec'] = '浙江'
        d['city'] = '宁波'
        dic['obj'] = d
    elif request.method == "POST":
        dic = {}
        d = {}
        dic['success'] = True
        d['proviec'] = '浙江'
        d['city'] = '宁波'
        dic['obj'] = d
    return HttpResponse(json.dumps(dic,ensure_ascii=False))

@csrf_exempt
def faceList(request):
    print(request.body)
    dic = {}
    d = {}
    dic['success'] = True
    d['obj'] = ['20元', '30元', '50元']
    dic['obj'] = d
    return HttpResponse(json.dumps(dic,ensure_ascii=False))