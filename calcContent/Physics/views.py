from django.shortcuts import render
from django.http import JsonResponse
import math

# Create your views here.
def physicsMain(request):
    return render(request, 'physics.html')

def equations_of_motion(request):
    result = ''
    result1 = ''
    result2 = ''
    s1 = request.POST.get('s1')
    t1 = request.POST.get('t1')
    u1 = request.POST.get('u1')
    v1 = request.POST.get('v1')
    a1 = request.POST.get('a1')

    if request.method == 'POST':
        if 's1' in request.POST:
            if 't1' in request.POST:
                if 'u1' in request.POST:
                    result = 2*((s1-(u1*t1))/(t1)**2)   #calculation of second 'a'
                elif 'a1' in request.POST:
                    result = (s1 - 0.5*a1*(t1)**2)/t1     #calculation of second 'u'
            elif 'u1' in request.POST:
                if 'v1' in request.POST:
                    result = ((v1)**2 - (u1)**2)/(2*s1) #calculation of third 'a'
                elif 'a1' in request.POST:
                    result = (u1)**2 + 2*a1*s1  #calculation of third 'v'
            elif 'v1' in request.POST:
                result = ((v1)**2 - (2*a1*s1))**(1/2)   #calculation of third 'u'
        elif 't1' in request.POST:
            if 'u1' in request.POST:
                if 'v1' in request.POST:
                    result = (v1-u1)/t1 #calculation of first 'a'
                elif 'a1' in request.POST:
                    result = u1+(a1*t1) #calculation of first 'v'
                    result1 = (u1*t1)+(0.5*a1*(t1)**2)  #calculation of second 's'
            if 'v1' in request.POST:
                if 'a1' in request.POST:
                    result = v1 - (a1*t1)   #calculation of first 'u'
        elif 'u1' in request.POST:
            if 'a1' in request.POST:
                if 'v1' in request.POST:
                    result = (v1-u1)/a1 #calculation of first 't'
                    result2 = ((v1)**2 - (u1)**2)/(2*a1)    #calculation of third 's'
                elif 's1' in request.POST:
                    result = (-u1+((u1**2)+(2*a1*s1))**(1/2))/a1    #calculation of second 't'
        
    context = {
        'result': result,
        'result1': result1,
        'result2': result2,
    }
    return render(request, 'kinematics.html', context=context)

def proj_motion(request):
    x = ''
    result = ''
    result1 = ''
    result2 = ''
    result3 = ''
    result4 = ''
    result5 = ''
    t1 = request.POST.get('t1')
    u1 = request.POST.get('u1')
    h1 = request.POST.get('h1')
    r1 = request.POST.get('r1')
    g1 = request.POST.get('g1')
    x1 = request.POST.get('x1')
    uc1 = request.POST.get('uc1')
    us1 = request.POST.get('us1')

    x2 = math.radians(x1)
    x3 = x2 * 2
            
    if request.method == 'POST':
        if 't1' in request.POST:
            if 'u1' in request.POST:
                x = (t1*g1)/(2*u1)
                result = math.degrees(math.asin(x)) #calculation of x1
            elif 'x1' in request.POST:
                result = (t1*g1)/(2*(math.sin(x2))) #calculation of u1
        elif 'u1' in request.POST:
            result = (2*u1*(math.sin(x2)))/g1   #calculation of t1
            result1 = (((u1)**2)*(math.sin(x2))**2)/(2*g1)  #calculation of h1
            result2 = ((u1)**2)*(math.sin(x3))/g1   #calculation of r1
            result3 = u1*(math.cos(x2)) #calculation of uc1
            result4 = u1*(math.sin(x2)) #calculation of us1
            result5 = (u1*(math.sin(x2)))/g1   #calculation of ta1
            if 'h1' in request.POST:
                x = (h1*2*g1)/((u1)**2)
                result = (math.degrees(math.asin(x)))**(1/2)    #calculation of x2
            elif 'r1' in request.POST:
                x = (r1*g1)/(u1**2)
                result = (math.degrees(math.asin(x)))/2 #calculation of x3
        elif 'h1' in request.POST:
            if 'x1' in request.POST:
                result = ((h1*2*g1)**(1/2))/(math.sin(x2))  #calculation of u2
            else:
                result = ((2*h1)/g1)**(1/2) #calculation of td1
        elif 'r1' in request.POST:
            result = ((r1*g1)/math.sin(x3))**(1/2)  #calculation of u3
        elif 'uc1' in request.POST:
            result = math.degrees(math.atan2(us1, uc1)) #calculation of x7

    context = {
        'result': result,
        'result1': result1,
        'result2': result2,
        'result3': result3,
        'result4': result4,
        'result5': result5,
    }
    return render(request, 'kinematics.html', context=context)