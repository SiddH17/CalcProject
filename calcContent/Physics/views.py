from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def equations_of_motion(request):
    result = ''
    result1 = ''
    result2 = ''
    s1 = float(request.POST.get('s1'))
    t1 = float(request.POST.get('t1'))
    u1 = float(request.POST.get('u1'))
    v1 = float(request.POST.get('v1'))
    a1 = float(request.POST.get('a1'))

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