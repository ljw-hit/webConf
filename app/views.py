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
    linkStr = request.GET.get("Data")
    links = linkStr.split(",")
    switch.choiceLink(links)
    result = {}
    result["data"] = "s"
    return JsonResponse(result)


