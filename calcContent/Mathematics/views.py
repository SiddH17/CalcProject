from django.shortcuts import render
from django.http import JsonResponse
import numpy as np
import math

# Create your views here.
def mathematicsMain(request):
    return render(request, 'mathematics.html')

def trigonometry(request):
    return render(request, 'trigonometry.html')

def parabola(request):
    return render(request, 'parabola.html')

def ellipse(reqest):
    return render(reqest, 'ellipse.html')

def hyperbola(request):
    return render(request, 'hyperbola.html')

def statistics(request):
    return render(request, 'statistics.html')

# APIs
def trigonometry_api(request):
    valueSelected = request.GET.get('select_value')
    a = float(request.GET.get('angle1'))
    b = float(request.GET.get('angle2'))
    s = 0

    a=a*0.0174533
    b=b*0.0174533   
    print(valueSelected, "The value selected")

    if valueSelected == 'sin(a+b)':
        s=(math.sin(a)*math.cos(b))+(math.cos(a)*math.sin(b))
    elif valueSelected == 'sin(a-b)':
        s=(math.sin(a)*math.cos(b))-(math.cos(a)*math.sin(b))
    elif valueSelected == 'cos(a+b)':
        s=(math.cos(a)*math.cos(b))-(math.sin(a)*math.sin(b))
    elif valueSelected == 'cos(a-b)':
        s=(math.cos(a)*math.cos(b))+(math.sin(a)*math.sin(b))
    elif valueSelected == 'tan(a+b)':
        s=(math.tan(a)+math.tan(b))/(1-(math.tan(a)*math.tan(b)))
    elif valueSelected == 'tan(a-b)':
        s=(math.tan(a)-math.tan(b))/(1+(math.tan(a)*math.tan(b))) 

    context = {
        'result': s
    }
    return JsonResponse(context)

def ellipse_api(request):
    a = float(request.GET.get('ecc2a'))
    b = float(request.GET.get('ecc2b'))
    e=0

    if a>b:
        e=math.sqrt(((a*a)-(b*b))/(a**2))

    elif a<b:
        e=math.sqrt(((b*b)-(a*a))/(b**2))

    context = {
        'result': e
    }

    return JsonResponse(context)

def hyperbola_api(request):
    a = float(request.GET.get('ecc2a'))
    b = float(request.GET.get('ecc2b'))
    e=0

    e=math.sqrt(((a*a)+(b*b))/(a**2))

    context = {
        'result': e
    }

    return JsonResponse(context)

