from django.shortcuts import render
from django.http import JsonResponse
import numpy as np
import math, statistics

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

def stats(request):
    return render(request, 'statistics.html')

def quadratics(request):
    return render(request, 'quadratics.html')

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

def statistics_api(request):
    valueSelected = request.GET.get('select_value')
    n = int(request.GET.get('obs'))
    numbers = request.GET.get('nums','').strip()
    result = 0
    print("The selected value: ", valueSelected)
    print(n)

    numbers = [float(num) for num in numbers.split()]
    print(numbers)

    if n == len(numbers):
        if valueSelected == 'mean':
            result = sum(numbers)/n
        elif valueSelected == 'median':
            numbers.sort()
            if n%2==0:
                result = (numbers[int((n+1)/2)]+numbers[int((n-1)/2)])/2
            else:
                result = numbers[int(n/2)]
        elif valueSelected == 'mode':
            result = statistics.mode(numbers)
    else:
        result = None

    context = {
        'result': result
    }

    return JsonResponse(context)

def quadratics_api(request):
    #Defining values obtained from frontend
    a = int(request.GET.get('a_value'))
    b = int(request.GET.get('b_value'))
    c = int(request.GET.get('c_value'))
    error = ''

    solution = f"{a}x^2 + {b}x + {c}"
    print(solution)
    
    #Calculating both roots of the equation
    root = (b**2 - 4*a*c)
    root1 = root2 = None

    if root>=0:
        root1 = float((b+math.sqrt(root))/(2*a))
        root2 = float((b-math.sqrt(root))/(2*a))
    else:
        error = 'Root does not exist as Discriminant < 0'

    context = {
        'root': root,
        'root1': root1,
        'root2': root2,
        'solution': solution,
        'error': error
    }

    return JsonResponse(context)

