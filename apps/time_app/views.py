from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime, localtime

def index(request):
  context = {
  "test": strftime("%b %d %Y", localtime()),
  "test2": strftime("%H:%M %p", localtime())
  }
  return render(request,'time_app/index.html', context)
