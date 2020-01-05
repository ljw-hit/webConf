from django.shortcuts import render
from django.http import JsonResponse
from dataFromFile import getIp
from  django.views.decorators.csrf import csrf_exempt
import switch
# Create your views here.
def getIndex(request):
    return render(request,"index.html")

def ipMess(request):
    result = {"data":getIp.ipData()}
    return JsonResponse(result)

def startproxy(request):
    links = request.GET.get("Data")
    print(links)
    links = links.split(",")
    linkMess = switch.choiceLink(links)
    result = {"data":linkMess}
    return  JsonResponse(result)

def delayTime(request):
    links = request.GET.get("Data")
    #print(links)
    links = links.split(",")
    linkMess = switch.delay(links)
    result = {"data": linkMess}
    return JsonResponse(result)