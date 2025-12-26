from django.shortcuts import render
from django.http import JsonResponse
import math

# Create your views here.
def physicsMain(request):
    return render(request, 'physics.html')

#Equations of motion view
def equations_of_motion(request):
    return render(request, 'kinematics.html')

#Projectile motion view
def proj_motion(request):
    return render(request, 'kinematics.html')

#Thermodynamics page view
def thermodynamics(request):
    return render(request, 'thermodynamics.html')

#Electrostatics page view
def electrostatics(request):
    return render(request, 'electrostatics.html')

#Ray Optics page view
def rayOptics(request):
    return render(request, 'rayoptics.html')

#Current Electricity page view
def currentElectricity(request):
    return render(request, 'current.html')

#Modern Physics page view
def modern_physics(request):
    return render(request, 'modPhysics.html')

#Electromagnetic Induction page view
def emi(request):
    return render(request, 'emi.html')

#Wave Optics page view
def wave_optics(request):
    return render(request, 'waveOptics.html')

#Circular Motion page view
def circular_motion(request):
    return render(request, 'circmotion.html')

# APIs
#Kinematics API views
def equations_of_motion_api(request):
    if request.method == 'GET':
        result = None
        s1 = request.GET.get('s1')
        t1 = request.GET.get('t1')
        u1 = request.GET.get('u1')
        v1 = request.GET.get('v1')
        a1 = request.GET.get('a1')
        selectedDiv = request.GET.get('selectedDiv')
        
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

        print(selectedDiv, "This is the selected div right now!")
        if s1:
            if t1:
                if u1:
                    result = 2*((s1-(u1*t1))/(t1)**2)   #calculation of second 'a'
                elif a1:
                    result = (s1 - 0.5*a1*(t1)**2)/t1     #calculation of second 'u'
            elif u1:
                if v1:
                    result = ((v1)**2 - (u1)**2)/(2*s1) #calculation of third 'a'
                elif a1:
                    result = (u1)**2 + 2*a1*s1  #calculation of third 'v'
            elif v1:
                if a1:
                    result = ((v1)**2 - (2*a1*s1))**(1/2)   #calculation of third 'u'
        elif t1:
            if u1:
                if v1:
                    result = (v1-u1)/t1 #calculation of first 'a'
                elif a1:
                    if selectedDiv == 'firstfinvel':         
                        result = u1+(a1*t1) #calculation of first 'v'
                    elif selectedDiv == 'seconddisp':  
                        result = (u1*t1)+(0.5*a1*(t1)**2)  #calculation of second 's'
            elif v1:
                if a1:
                    result = v1 - (a1*t1)   #calculation of first 'u'
        elif u1:
            if v1:
                if a1:
                    if selectedDiv == 'firsttime':
                        result = (v1-u1)/a1 #calculation of first 't'
                    elif selectedDiv == 'thirddisp':
                        result = ((v1)**2 - (u1)**2)/(2*a1)    #calculation of third 's'
            elif s1:
                if a1:
                    result = (-u1+((u1**2)+(2*a1*s1))**(1/2))/a1    #calculation of second 't'

        print(result, "The first and only result, result")
        context = {
            'result': result,
        }
        return JsonResponse(context)

def proj_motion_api(request):
    if request.method == 'GET':
        result1 = None
        t1 = request.GET.get('t1')
        u1 = request.GET.get('u1')
        h1 = request.GET.get('h1')
        r1 = request.GET.get('r1')
        g1 = request.GET.get('g1')
        x1 = request.GET.get('x1')
        uc1 = request.GET.get('uc1')
        us1 = request.GET.get('us1')
        projSelectedDiv = request.GET.get('projSelectedDiv')

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
            g1 = float(g1)
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

        if t1:
            if u1:
                x = (t1*g1)/(2*u1)
                result1 = math.degrees(math.asin(x)) #calculation of x1
            elif x1:
                result1 = (t1*g1)/(2*(math.sin(x1))) #calculation of u1
        elif u1:
            if x1:
                if g1:
                    if projSelectedDiv == 'fsttof':
                        result1 = (2*u1*(math.sin(math.degrees(x1))))/g1   #calculation of t1
                    elif projSelectedDiv == 'secheight':
                        result1 = (((u1)**2)*(math.sin(math.degrees(x1)))**2)/(2*g1)  #calculation of h1
                    elif projSelectedDiv == 'trdrange':
                        result1 = ((u1)**2)*(math.sin(x1))/g1   #calculation of r1
                    elif projSelectedDiv == 'fourthhorver':
                        result1 = u1*(math.cos(x1)) #calculation of uc1
                    elif projSelectedDiv == 'fifthhorver':
                        result1 = u1*(math.sin(x1)) #calculation of us1
                    elif projSelectedDiv == 'eighthtad':
                        result1 = (u1*(math.sin(x1)))/g1   #calculation of ta1
            elif h1:
                x = (h1*2*g1)/((u1)**2)
                result1 = (math.degrees(math.asin(x)))**(1/2)    #calculation of x2
            elif r1:
                x = (r1*g1)/(u1**2)
                result1 = (math.degrees(math.asin(x)))/2 #calculation of x3
        elif h1:
            if x1:
                result1 = ((h1*2*g1)**(1/2))/(math.sin(x1))  #calculation of u2
            elif g1:
                result1 = ((2*h1)/g1)**(1/2) #calculation of td1
        elif r1:
            result1 = ((r1*g1)/math.sin(x1))**(1/2)  #calculation of u3
        elif uc1:
            result1 = math.degrees(math.atan2(us1, uc1)) #calculation of x7

    print("The result of projectile motion, ", result1)
    context = {
        'result1': result1,
    }
    return JsonResponse(context)

# electrostatics API views
def electrostatics_api(request):
    valueSelected = request.GET.get('select_value')
    F = float(request.GET.get('F'))
    Q = float(request.GET.get('Q'))
    q = float(request.GET.get('q'))
    r = float(request.GET.get('r'))

    print(valueSelected, "This is the value that has been selected eventually")
    k=1/(4*math.pi*8.854187817e-12)
    result = None

    if valueSelected == 'force':
        result = (k*q*Q)/r

    elif valueSelected == 'charge2':
        result = (F*r)/(k*Q)

    elif valueSelected == 'charge1': 
        result = (F*r)/(k*q)
        
    elif valueSelected == 'distance':
        result = (k*q*Q)/F

    context = {
        'result': result,
    }
    return JsonResponse(context)

def mirror_api(request):
    f = float(request.GET.get('fl'))
    v = float(request.GET.get('imgdist'))
    u = float(request.GET.get('objdist'))
    result = None

    select_value = request.GET.get('select_value')
    mirror_type = request.GET.get('mirror_type')

    #this is to convert positive into negative values for some, if not done already
    if u>0:   #object distance is always negative
        u = -abs(u)
    if v>0 and mirror_type=='convex': #in case of concave mirrors, image distance is always negative
        v = -abs(v)
    if f>0 and mirror_type=='concave':    #focal length is always negative in concave mirrors
        f = -abs(f)
    if f>v and mirror_type=='concave':  #image distance is negative when less than the focal length of a concave mirror
        v = -abs(v)  

    #calculating the respective results
    if select_value == 'focal':
        result = (u*v)/(u+v)
    elif select_value == 'virtual':
        result = (f*u)/(u-f)
        if (u>f and mirror_type=='concave') or (mirror_type == 'convex'):    #image distance is negative when object is placed between focus and pole
            print("We have entered the sacred function")
            result = -abs(result)
            print(result)
    elif select_value == 'real':
        result = (f*v)/(v-f)


    context = {
        'result': result,
    }
    return JsonResponse(context)

def lens_api(request):
    f = float(request.GET.get('lfl'))
    v = float(request.GET.get('lensimgdist'))
    u = float(request.GET.get('lensobjdist'))
    result = None

    select_value = request.GET.get('select_value')
    lens_type = request.GET.get('lens_type')

    #this is to convert positive into negative values for some, if not done already
    if u>0:   #object distance is always negative
        u = -abs(u)
    if v>0 and lens_type=='concave': #in case of concave lenses, image distance is always negative
        v = -abs(v)
    if f>0 and lens_type=='concave':    #focal length is always negative in concave lenses
        f = -abs(f)
    if f>v and lens_type=='concave':  #image distance is negative when less than the focal length of a concave lens
        v = -abs(v)
    
    if select_value == 'focal':
        result = (u*v)/(u-v)
    elif select_value == 'virtual':
        result = (f*u)/(f+u)
        if (u>f and lens_type == 'convex') or (lens_type == 'concave'):
            result = -abs(result)
    elif select_value == 'real':
        result = (f*v)/(f-v)

    
    
    context = {
        'result': result
    }

    return JsonResponse(context)

#Current Electricity API views
def ohms_law_api(request):
    #Selected dropdown value
    valueSelected = request.GET.get('select_value')

    #All required numerical values
    v = float(request.GET.get('voltage'))
    i = float(request.GET.get('current'))
    r = float(request.GET.get('resistance'))
    result = None

    if valueSelected == 'voltage':
        result = r*i
        result = str(result)
        result += ' V'
    elif valueSelected == 'current':
        result = v/r
        result = str(result)
        result += ' A'
    elif valueSelected == 'resistance':
        result = v/i
        result = str(result)
        result += ' ohm'

    context = {
        'result': result
    }

    return JsonResponse(context)

def power_api(request):
    valueSelected = request.GET.get('select_value')
    rSelect = request.GET.get('resistance_select')
    pSelect = request.GET.get('power_select')

    p = float(request.GET.get('power'))
    v = float(request.GET.get('voltage'))
    i = float(request.GET.get('current'))
    r = float(request.GET.get('resistance'))
    result = None

    if valueSelected == 'power':
        if pSelect == 'f1':
            result = v*i
        elif pSelect == 'f2':
            result = (i**2)*r
        elif pSelect == 'f3':
            result = (v**2)/r
        result = str(result)
        result += ' W'
    elif valueSelected == 'resistance':
        if rSelect == 'f4':
            result = (i**2)/p
        elif rSelect == 'f5':
            result = (v**2)*p
        result = str(result)
        result += ' ohm'

    context = {
        'result': result
    }

    return JsonResponse(context)

def resistivity_api(request):
    valueSelected = request.GET.get('select_value')

    rho = float(request.GET.get('rho'))
    r = float(request.GET.get('rest'))
    l = float(request.GET.get('length'))
    a = float(request.GET.get('area'))
    result = None

    if valueSelected == 'resistivity':
        result = (r*a)/l
        result = str(result)
        result += ' ohm*m'
    elif valueSelected == 'resistance':
        result = (rho*l)/a
        result = str(result)
        result += ' ohm'
    elif valueSelected == 'conductance':
        result = 1/rho
        result = str(result)
        result += ' S'

    context = {
        'result': result
    }
    print(result)

    return JsonResponse(context)

def heat_and_energy_api(request):
    valueSelected = request.GET.get('select_value')
    heatValue = request.GET.get('heat_select')

    v = float(request.GET.get('v'))
    i = float(request.GET.get('i'))
    r = float(request.GET.get('r'))
    t = float(request.GET.get('t'))
    result = None

    if valueSelected == 'energy':
        result = (1/2)*(v**2)*(i)
    elif valueSelected == 'heat':
        if heatValue == 'heat1':
            result = ((v*2)*t)/r
        elif heatValue == 'heat2':
            result = (i**2)*r*t

    result = str(result)
    result += ' Joules'

    context = {
        'result': result
    }

    return JsonResponse(context)

#Thermodynamics API Views
def equipartition_of_energy(request):
    tempUnit = request.GET.get('tempUnit')

    n = float(request.GET.get('dof'))
    t = float(request.GET.get('temperature'))
    k = 1.38e-23
    result = None

    if tempUnit == 'celsius':
        t = 273 + t

    result = (n/2)*k*t
    result = str(result)
    result += ' Joules'

    context = {
        'result': result
    }

    return JsonResponse(context)

#Modern Physics API Views
def debroglie_wavelength(request):
    valueSelected = request.GET.get('dbw_select')

    p = float(request.GET.get('p'))
    m = float(request.GET.get('ma'))
    v = float(request.GET.get('vel'))
    h = 6.626e-34
    result = None

    if valueSelected == 'dbw1':
        result = h/p
    elif valueSelected == 'dbw2':
        result = h/(m*v)

    result = str(result)
    result += ' m'

    return JsonResponse({'result': result})

def ev_joule_conversion(request):
    selectedValue = request.GET.get('value_select')

    ev = float(request.GET.get('ev'))
    j = float(request.GET.get('j'))
    result = None

    if selectedValue == 'eV':
        result = ev*1.6e-19
        result = str(result)
        result += ' Joules'
    elif selectedValue == 'joules':
        result = j/1.6e-19
        result = str(result)
        result += ' eV'

    return JsonResponse({'result': result})

def bohr_model(request):
    selectedValue = request.GET.get('value_select')

    z = float(request.GET.get('z'))
    n = float(request.GET.get('n'))
    e = -13.6
    a = 0.529e-10
    result = None

    if selectedValue == 'energy':
        result = e*((z**2)/n**2)
        result = str(result)
        result += ' MeV'
    elif selectedValue == 'radius':
        result = ((n**2)/z)*a

    return JsonResponse({'result': result})

def be_md(request):
    valueSelected = request.GET.get('value_select')

    z = float(request.GET.get('z'))
    n = float(request.GET.get('n'))
    ma = float(request.GET.get('ma'))
    a = float(request.GET.get('a'))
    result = None

    mp = 1.007276
    mn = 1.008665
    c = 3e8

    if valueSelected == 'binding-energy':
        result = ((z*mp)+(n*mn)-ma)*c**2
        result = str(result)
        result += ' MeV'
    elif valueSelected == 'mass-defect':
        result = (z*mp)+((a-z)*mn)-ma
        result = str(result)
        result += ' MeV/c^2'
    elif valueSelected == 'atomic-mass':
        result = z+n
        result = str(result)
        result += ' u'

    return JsonResponse({'result': result})

#Electromagnetic Induction API Views
def inductance_api(request):
    mu = float(request.GET.get('perm'))
    n = float(request.GET.get('turns'))
    l = float(request.GET.get('length'))
    a = float(request.GET.get('area'))
    result = None

    result = (mu*(n**2)*a)/l
    result = str(result)
    result += ' H'

    return JsonResponse({'result': result})

#Wave Optics API Views
def wavelength_frequency(request):
    valueSelected = request.GET.get('select_value')

    c = 3e8
    l = float(request.GET.get('w'))
    f = float(request.GET.get('f'))
    result = None

    if valueSelected == 'wavelength':
        result = c/f
        result = str(result)
        result += ' m'
    elif valueSelected == 'frequency': 
        result = c/l
        result = str(result)
        result += ' Hz'

    return JsonResponse({'result': result})

#Rydberg Formula API
def rydberg_formula(request):
    r=1.1e7
    n1=float(request.GET.get('n1'))
    n2=float(request.GET.get('n2'))
    result = None

    result = (1/r)*(1/n1**2 - 1/n2**2)
    result = str(result)
    result += ' m'

    return JsonResponse({'result': result})

#Angular Displacement, Velocity and Acceleration calculation API
def angular_api(request):
    #Get the required div value that is active
    value_div = request.GET.get('selectedDiv')
    #Get the dropdown formula value from frontend that has been selected
    value_select = request.GET.get('selectValue')
    result = None

    if value_div == 'angDispDiv':
        if value_select == 'sr':
            result = int(request.GET.get('disp')) / int(request.GET.get('radius'))
        elif value_select == 'wt':
            result = int(request.GET.get('angularVelocity')) * int(request.GET.get('time'))
    elif value_div == 'angVelDiv':
        if value_select == 'thetat':
            result = int(request.GET.get('theta')) / int(request.GET.get('time'))
        elif value_select == 'vr':
            result = int(request.GET.get('vel')) / int(request.GET.get('radius'))
    elif value_div == 'angAccDiv':
        if value_select == 'ar':
            result = int(request.GET.get('acc')) / int(request.GET.get('radius'))
        elif value_select == 'omegat':
            result = int(request.GET.get('angularVelocity')) / request.GET.get('time')

    print(result)

    return JsonResponse({'result': result})

#Banking of Roads API
def banking_api(request):
    valueSelect = request.GET.get('selectValue')
    m = float(request.GET.get('mass'))
    r = float(request.GET.get('radius'))
    v = float(request.GET.get('maxvel'))
    theta = float(request.GET.get('angle_banking'))
    theta = math.radians(theta)
    print(theta)
    g = 9.8

    result = None
    
    if valueSelect == 'max_velocity':
        result = (r*g*math.tan(theta))**(1/2)
    elif valueSelect == 'fric_force':
        result = (m*(v)**2)/r
    elif valueSelect == 'angle_of_banking':
        result = (v)**2/(r*g)

    print(result, "The result of the calculation")

    return JsonResponse({'result': result})

#Vertical Circular Motion API
def vertical_circular_motion_api(request):
    valueSelect = request.GET.get('valueSelect')
    posSelect = request.GET.get('posSelect')

    v = float(request.GET.get('velocity-vertical'))
    l = float(request.GET.get('length'))
    g = 9.8
    result = None

    if valueSelect == 'vertical-velocity':
        if posSelect == 'top':
            result = (g*l)**(1/2)
        elif posSelect == 'middle':
            result = (3*g*l)**(1/2)
        elif posSelect == 'bottom':
            result = (5*g*l)**(1/2)
    elif valueSelect == 'length':
        if posSelect == 'top':
            result = ((v)**2)/g
        elif posSelect == 'middle':
            result = ((v)**2)/(3*g)
        elif posSelect == 'bottom':
            result = ((v)**2)/(5*g)

    return JsonResponse({'result': result})
        
#Snell's Law API
def snells_law_api(request):
    dropdown_value = request.GET.get('snell_value')
    formula_value = request.GET.get('snell_formula')

    v1 = float(request.GET.get('v1Value'))
    v2 = float(request.GET.get('v2Value'))
    n1 = float(request.GET.get('n1Value'))
    n2 = float(request.GET.get('n2Value'))
    inc = float(request.GET.get('aoiValue'))
    ref = float(request.GET.get('aorValue'))

    result = None
    


