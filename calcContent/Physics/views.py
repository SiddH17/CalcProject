from django.shortcuts import render
from django.http import JsonResponse
import math

# Create your views here.
def physicsMain(request):
    return render(request, 'physics.html')

#Equations of motion view
def equations_of_motion(request):
    return render(request, 'kinematics.html')

#Equations of motion API view
def equations_of_motion_api(request):
    if request.method == 'GET':
        result = None
        s1 = request.GET.get('s1')
        t1 = request.GET.get('t1')
        u1 = request.GET.get('u1')
        v1 = request.GET.get('v1')
        a1 = request.GET.get('a1')
        
        if s1:
            print("s1 is real!", s1)
            s1 = int(s1)
        else:
            print("Welp, never mind")
        if t1:
            print("t1 is real!", t1)
            t1 = int(t1)
        else:
            print("Welp, never mind")        
        if u1:
            print("u1 is real!", u1)
            u1 = int(u1)
        else:
            print("Welp, never mind")        
        if v1:
            print("v1 is real!", v1)
            v1 = int(v1)
        else:
            print("Welp, never mind")        
        if a1:
            print("a1 is real!", a1)
            a1 = int(a1)
        else:
            print("Welp, never mind")

        if s1:
            print("Entered the s1 zone")
            if t1:
                print("Entered the t1 zone")
                if u1:
                    print("Entered the u1 zone")
                    result = 2*((s1-(u1*t1))/(t1)**2)   #calculation of second 'a'
                elif a1:
                    print("Entered the a1 zone")
                    result = (s1 - 0.5*a1*(t1)**2)/t1     #calculation of second 'u'
            elif u1:
                print("Entered the u1 zone")
                if v1:
                    print("Entered the v1 zone")
                    result = ((v1)**2 - (u1)**2)/(2*s1) #calculation of third 'a'
                elif a1:
                    print("Entered the a1 zone")
                    result = (u1)**2 + 2*a1*s1  #calculation of third 'v'
            elif v1:
                print("Entered the v1 zone")
                if a1:
                    print("Entered the a1 zone")
                    result = ((v1)**2 - (2*a1*s1))**(1/2)   #calculation of third 'u'
        elif t1:
            print("Entered the t1 zone")
            if u1:
                print("Entered the u1 zone")
                if v1:
                    print("Entered the v1 zone")
                    result = (v1-u1)/t1 #calculation of first 'a'
                elif a1:
                    print("Entered the a1 zone")        
                    result = u1+(a1*t1) #calculation of first 'v'
            elif v1:
                print("Entered the v1 zone")
                if a1:
                    print("Entered the a1 zone")
                    result = v1 - (a1*t1)   #calculation of first 'u'
        elif u1:
            print("Entered the u1 zone")
            if t1:
                print("Entered the t1 zone!")
                if a1:
                    print("Entered the a1 zone!")
                    result = (u1*t1)+(0.5*a1*(t1)**2)  #calculation of second 's'
            elif v1:
                print("Entered the v1 zone")
                if a1:
                    print("Entered the a1 zone")
                    result = (v1-u1)/a1 #calculation of first 't'
            elif s1:
                print("Entered the s1 zone")
                if a1:
                    print("Entered the a1 zone")
                    result = (-u1+((u1**2)+(2*a1*s1))**(1/2))/a1    #calculation of second 't'
        elif v1:
            print("Entered the v1 zone!")
            if u1:
                print("Entered the u1 zone!")
                if a1:
                    print("Entered the a1 zone!")
                    result = ((v1)**2 - (u1)**2)/(2*a1)    #calculation of third 's'
        print(result, "The first result, result")
        context = {
            'result': result,
        }
        return JsonResponse(context)

#Projectile motion view
def proj_motion(request):
    return render(request, 'kinematics.html')

#Projectile motion API view
def proj_motion_api(request):
    if request.method == 'GET':
        result = None
        t1 = request.GET.get('t1')
        u1 = request.GET.get('u1')
        h1 = request.GET.get('h1')
        r1 = request.GET.get('r1')
        g1 = request.GET.get('g1')
        x1 = request.GET.get('x1')
        uc1 = request.GET.get('uc1')
        us1 = request.GET.get('us1')

        if t1:
            t1 = int(t1)
            print('t1 is real!!', t1)
        if u1:
            u1 = int(u1)
            print('u1 is real!!', u1)
        if h1:
            h1 = int(h1)
            print('h1 is real!!', h1)
        if r1:
            r1 = int(r1)
            print('r1 is real!!', r1)
        if g1:
            g1 = int(g1)
            print('g1 is real!!', g1)
        if x1:
            x1 = int(x1)
            print('x1 is real!!', x1)
        if uc1:
            uc1 = int(uc1)
            print('uc1 is real!!', uc1)
        if us1:
            us1 = int(us1)
            print('us1 is real!!', us1)

        if 't1':
            if 'u1':
                x = (t1*g1)/(2*u1)
                result = math.degrees(math.asin(x)) #calculation of x1
            elif 'x1':
                result = (t1*g1)/(2*(math.sin(x1))) #calculation of u1
        elif 'u1':
            result = (2*u1*(math.sin(x1)))/g1   #calculation of t1
            result1 = (((u1)**2)*(math.sin(x1))**2)/(2*g1)  #calculation of h1
            result2 = ((u1)**2)*(math.sin(x1))/g1   #calculation of r1
            result3 = u1*(math.cos(x1)) #calculation of uc1
            result4 = u1*(math.sin(x1)) #calculation of us1
            result5 = (u1*(math.sin(x1)))/g1   #calculation of ta1
            if 'h1':
                x = (h1*2*g1)/((u1)**2)
                result = (math.degrees(math.asin(x)))**(1/2)    #calculation of x2
            elif 'r1':
                x = (r1*g1)/(u1**2)
                result = (math.degrees(math.asin(x)))/2 #calculation of x3
        elif 'h1':
            if 'x1':
                result = ((h1*2*g1)**(1/2))/(math.sin(x1))  #calculation of u2
            else:
                result = ((2*h1)/g1)**(1/2) #calculation of td1
        elif 'r1':
            result = ((r1*g1)/math.sin(x1))**(1/2)  #calculation of u3
        elif 'uc1':
            result = math.degrees(math.atan2(us1, uc1)) #calculation of x7

    context = {
        'result': result,
    }
    return JsonResponse(context)