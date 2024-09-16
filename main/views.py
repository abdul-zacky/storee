from django.shortcuts import render, redirect   # Tambahkan import redirect di baris ini
from main.forms import ProductForm
from main.models import Product

# Create your views here.
def show_main(request):
    context = {
        'name' : 'Abdul Zacky',
        'npm': '2306214510',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)