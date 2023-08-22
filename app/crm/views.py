from django.shortcuts import render # noqaS

# Create your views here.
def home(request):
    return render(request, 'home.html', {})