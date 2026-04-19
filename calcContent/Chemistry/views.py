from django.shortcuts import render
from django.http import JsonResponse

import math

# Create your views here.
#Chemistry main page
def chemistryMain(request):
    return render(request, 'chemistry.html')

#Gaseous state
def gaseous(request):
    return render(request, 'gaseous.html')

#Chemical Thermodynamics
def chem_thermo(request):
    return render(request, 'chemThermo.html')

#API Views
#Gaseous state API
def gaseous_api(request):
    #Selected dropdown value
    selectedValue = request.GET.get('select_value')
    
    #All required numerical values
    p = float(request.GET.get('P'))
    v = float(request.GET.get('V'))
    n = float(request.GET.get('n'))
    t = float(request.GET.get('T'))
    result = None   #End result
    r = None    #Rate constant
    error = ''  #Error statement

    #Different units used
    pressure = request.GET.get('pressure')
    volume = request.GET.get('volume')
    temperature = request.GET.get('temperature')

    #Convert celsius to kelvin if recorded in the former
    if temperature == 'celsius':
        t = 273 + t

    #Define 'r' value based on the units used
    if volume == 'litre' or pressure == 'atm':
        r = 0.08206
    elif volume == 'm^3' or pressure == 'pascal':
        r = 8.314
    else:
        print("Error!")

    #Calculate pressure value
    if selectedValue == 'pressure':
        result = (n*r*t)/v
        result = str(result)

        if volume == 'litre':
            pressure = 'atm'
        elif volume == 'm^3':
            pressure = 'pascal'

        result = result + ' ' + pressure

    #Calculate volume value
    elif selectedValue == 'volume':
        result = (n*r*t)/p
        result = str(result)

        if pressure == 'atm':
            volume = 'litre'
        elif pressure == 'pascal':
            volume = 'm^3'
        
        result = result + ' ' + volume

    #Calculate no. of moles value
    elif selectedValue == 'mole':   
        result = (r*t)/(p*v)
        result = str(result)
        result = result + ' ' + 'moles'

    #Calculate temperature value
    elif selectedValue == 'temperature':
        result = (v*p)/(n*r)
        result = str(result)
        result = result + ' ' + 'K'

    #Passing a dictionary with result and error messages
    context = {
        'result': result
    }

    return JsonResponse(context)

def kineticTheory_api(request):
    #Selected dropdown value
    selectedValue = request.GET.get('select_value2')

    #Temperature unit
    temperature = request.GET.get('temperature2')

    #All required label values
    ke = float(request.GET.get('ke'))
    n = float(request.GET.get('n'))
    t = float(request.GET.get('t'))
    r = 8.314
    result = None

    #Convert celsius to kelvin
    if temperature == 'celsius':
        t += 273

    if selectedValue == 'kinetic-energy':
        result = (3/2)*n*r*t
        result = str(result)
        result = result + ' Joules'
    elif selectedValue == 'moles':
        result = ((2/3)*ke)/(r*t)
        result = str(result)
        result = result + ' moles'
    elif selectedValue == 'temp':
        result = ((2/3)*ke)/(r*n)
        result = str(result)
        result = result + 'K'

    context = {
        'result': result
    }

    return JsonResponse(context)

def rms_velocity_api(request):
    #Selected dropdown value
    selectedValue = request.GET.get('select_value3')

    #All required label units
    rms = float(request.GET.get('rms'))
    t = float(request.GET.get('t3'))
    m = float(request.GET.get('mm'))
    r = 8.314
    result = None

    #Temperature unit
    temperature = request.GET.get('temperature3')
    print(temperature)
    if temperature == 'celsius':
        t = 273 + t
        print(t, "The value of temperature in kelvin")

    if selectedValue == 'rms-velocity':
        result = math.sqrt((3*r*t)/m)
        result = str(result)
        result = result + ' m/s'
    elif selectedValue == 'temperature3':
        result = ((rms**2)*m)/(3*r)
        result = str(result)
        result = result = ' K'
    elif selectedValue == 'molar-mass':
        result = ((3*r*t)/(rms**2))
        result = str(result)
        result = result + ' kg/mol'
    
    context = {
        'result': result
    }

    return JsonResponse(context)

#Chemical Thermodynamics API
def internal_energy(request):
    t = float(request.GET.get('temperature'))
    m = int(request.GET.get('moles'))
    n = float(request.GET.get('dof'))
    r = 8.314

    temperature = request.GET.get('temperatureUnit')
    if temperature == 'celsius':
        t = 273 + t

    result = (m/2)*n*r*t
    result = str(result)
    result += ' J'

    return JsonResponse({'result': result})


