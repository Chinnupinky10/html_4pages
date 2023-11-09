from django.shortcuts import render

# Create your views here.

def puji(request):
    return render(request,'puji.html')

def sam(request):
    return render(request,'sam.html')

def ram(request):
    return render(request,'ram.html')

def pinky(request):
    return render(request,'pinky.html')