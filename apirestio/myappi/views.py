from django.shortcuts import render

# Create your views here.
def home(request):

    return render(request, 'pages/index.html')


def about(request):

    return render(request, 'pages/about.html')

def menu(request):

    return render(request, 'pages/menu.html')

def team(request):

    return render(request, 'pages/team.html')

def reservation(request):

    return render(request, 'pages/reservation.html')

def specialite(request):

    return render(request, 'pages/specialite.html')