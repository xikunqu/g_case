from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from backend.models import Data
import json,logging

# Create your views here.

@csrf_exempt
def add_data(request):
    if request.method=="POST":
        # print(request.body)
        # req=json.loads(request.body,strict=False)
        # logging.info(req)
        # key_flag=req.get("name") and req.get("data_type")
        # if key_flag:
        #     return JsonResponse({"status":"BS.100","msg":"publish article sucess."})
        print("request is ",request)
        print("body is ",request.body)
        name=request.POST.get("name")
        data_type=request.POST.get("data_type")
        case_id=request.POST.get("case")


        print(name)

        if name and data_type:
            add_da=Data(name=name,data_type=data_type,case=case_id)
            add_da.save()
            return  JsonResponse({"status":"BS.200","msg":"publish article sucess."})
        else:
            return JsonResponse({"status":"BS.300","msg":"publish article sucess."})

    else:
        return  JsonResponse({"status":"BS.400","msg":"error."})



def delete_data(request):
    pass

def update_data(request):
    pass

