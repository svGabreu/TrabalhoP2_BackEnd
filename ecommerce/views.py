#from django.shortcuts import render
from .models import Categoria, Produto
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy

#def ecommerce_app(request):
#    return render(request, "ecommerce/ecommerce_app.html")

class CriarCategoria(CreateView):
    model = Categoria
    fields = ["nome_categoria","descricao_categoria"]
    success_url = reverse_lazy("ecommerce_app")

class CriarProduto(CreateView):
    model = Produto
    fields = ["nome_produto","descricao_produto","preco","categoria","created_at"]
    success_url = reverse_lazy("ecommerce_app")

class UpdateProduto(UpdateView):
    model = Produto
    fields = ["nome_produto","descricao_produto","preco","categoria"]
    success_url = reverse_lazy("ecommerce_app")

class ProdutoListView(ListView):
    model = Produto

class ProdutoDeleteView(DeleteView):
    model = Produto
    success_url = reverse_lazy("ecommerce_app")
