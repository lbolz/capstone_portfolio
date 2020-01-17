from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "pages/home.html", {})

def creativity(request):
    return render(request, "pages/creativity.html", {})

def critical_thinking(request):
    return render(request, "pages/critical_thinking.html", {})

def career_management(request):
    return render(request, "pages/career_management.html", {})

def time_management(request):
    return render(request, "pages/time_management.html", {})

def professionalism(request):
    return render(request, "pages/professionalism.html", {})

def reflection(request):
    return render(request, "pages/reflection.html", {})
