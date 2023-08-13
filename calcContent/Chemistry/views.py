from django.shortcuts import render

# Create your views here.
def chemistryMain(request):
    return render(request, 'chemistry.html')