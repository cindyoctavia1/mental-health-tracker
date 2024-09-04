from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '23061165780',
        'name': 'Cindy Ocavia',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)
