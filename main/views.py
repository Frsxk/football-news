from django.shortcuts import render

# Create your views here.

def show_main(request):
    context = {
        'npm' : '2406496082',
        'name': 'Muhammad Faza Al-Banna',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)
