from django.shortcuts import render
from django.http import HttpResponse
import random

def index (request):
    return render(request,"toss.html")

def toss(request):
    result=random.choice(["Heads","Tails"])
    return render(request,"toss.html",{"result":result})
