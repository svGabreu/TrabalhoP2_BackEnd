from django.shortcuts import render
from .models import Categoria, Produto, Foto

def ecommerce_app(request):
    return render(request, "ecommerce/ecommerce_app.html")
