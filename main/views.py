from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name' : 'Abdul Zacky',
        'npm': '2306214510',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)