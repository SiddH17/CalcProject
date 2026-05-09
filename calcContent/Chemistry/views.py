from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

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

def mole_concept(request):
    return render(request, 'moleConcept.html')

def atomic_structure(request):
    return render(request, 'atom-structure.html')

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

#Ideal Gas Equation (Mole Concept) API
def ideal_gas_equation_mole(request):
    selectValue = request.GET.get('select_value')
    tempUnit = request.GET.get('temperatureUnit')
    pressureUnit = request.GET.get('pressureUnit')
    p = float(request.GET.get('pressureLabel'))
    v = float(request.GET.get('volumeLabel'))
    n = float(request.GET.get('molesLabel'))
    t = float(request.GET.get('temperatureLabel'))

    if tempUnit == 'celsius':
        t += 273
        print(t, "Converted value in Kelvin")

    result = None
    r = None
    if pressureUnit == 'atm':
        r = 0.0821
    elif pressureUnit == 'bar':
        r = 0.0833

    if selectValue == 'pressure':
        result = (n*r*t)/v
    elif selectValue == 'volume':
        result = (n*r*t)/p
    elif selectValue == 'moles':
        result = (p*v)/(r*t)
    elif selectValue == 'temperature':
        result = (p*v)/(n*r)

    return JsonResponse({'result': result})

#Hydrogen Spectrum API
@api_view(['GET'])
def hydrogen_structure_api(request):
    select_value = request.GET.get('select_value')
    l = float(request.GET.get('wavelengthLabel'))
    n1 = float(request.GET.get('n1Label'))
    n2 = float(request.GET.get('n2Label') or 0)
    print(n2, "The value of n2")

    r = 1.097*(10)**7
    result = result1 = result2 = None

    if select_value == 'wavelength':
        print("I'm atleast in the wavelength section now")
        if n2==0:
            print("Inside the if n2 is zero function")
            result1 = 1/(r*((1/(n1)**2)-(1/(n1+1)**2)))
            result2 = 1/(r*((1/(n1)**2)))
        else:
            print("I'm in the else section to execute the function")
            if n2<=n1:
                return Response({
                    'status': '400',
                    'message': 'Value of n2 must be greater than n1! Please try again.',
                },
                status=status.HTTP_400_BAD_REQUEST)
            else:
                result = 1/(r*((1/(n1)**2)-(1/(n2)**2)))
    elif select_value == 'n1':
        result = math.sqrt(1/((1/(l*r))+(1/(n2)**2)))
    elif select_value == 'n2':
        result = math.sqrt(1/((1/(n1)**2)-(1/(l*r))))

    return JsonResponse({'result': result, 'result1': result1, 'result2': result2})

#Bohr's Model API
def bohr_model_api(request):
    select_value = request.GET.get('select_value')
    formula_val = request.GET.get('formula_value')

    rn = float(request.GET.get('rn'))
    vn = float(request.GET.get('vn'))
    en = float(request.GET.get('en'))
    z = float(request.GET.get('az'))
    n = float(request.GET.get('qn'))

    result = None

    if select_value == 'radius':
        result = (0.529*(10**-10))*((n**2)/z)
    elif select_value == 'velocity':
        result = (2.18*(10**6))*(z/n)
    elif select_value == 'energy':
        result = (-13.6)*((z**2)/(n**2))
    elif select_value == 'atomic-number':
        if formula_val == 'radius-formula':
            result = (0.529*(10**-10))*((n**2)/rn)
        elif formula_val == 'velocity-formula':
            result = (n*vn)/(2.18*(10**6))
        elif formula_val == 'energy-formula':
            result = math.sqrt(((n**2)*en)/(-13.6))
    elif select_value == 'quantum-number':
        if formula_val == 'radius-formula':
            result = (z*rn)/(0.529*(10**-10))
        elif formula_val == 'velocity-formula':
            result = (z*(2.18*(10**6)))/vn
        elif formula_val == 'energy-formula':
            result = math.sqrt((z**2)*(-13.6)/en)

    return JsonResponse({'result': result})

