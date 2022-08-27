from django.shortcuts import render
from .models import AboutPage

# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    try:
        data = AboutPage.objects.get(id=2)
        return render(request, 'about.html', {'context':data})
    except Exception as err:
        #print(err)
        return render(request, 'about.html', {'error': 'Unable to load data!'})

def contact(request):
    return render(request, 'contact.html')

def services(request):
    return render(request, 'services.html')

def resume(request):
    return render(request, 'resume.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def portfolioDetails(request):
    return render(request, 'portfolio-details.html')