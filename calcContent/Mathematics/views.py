from django.shortcuts import render

# Create your views here.
def mathematicsMain(request):
    return render(request, 'mathematics.html')