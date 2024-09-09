from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name' : 'Macbook Pro',
        'price': '20000',
        'description': 'Macbook Pro, So Pro'
    }

    return render(request, "main.html", context)