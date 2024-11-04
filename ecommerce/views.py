from django.shortcuts import render
from .models import Categoria, Produto
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy

#def ecommerce_app(request):
#    ecommerce = ecommerce.objects.all()
#    return render(request, "ecommerce/ecommerce_app.html", {"ecommerce": ecommerce})

def ecommerce_list(request):
    return render(request, "ecommerce/ecommerce_list.html")

class CriarCategoria(CreateView):
    model = Categoria
    fields = ["nome","descricao"]
    success_url = reverse_lazy("criar_categoria")

class CriarProduto(CreateView):
    model = Produto
    fields = ["nome","descricao","preco","categoria","created_at"]
    success_url = reverse_lazy("criar_produto")

class UpdateProduto(UpdateView):
    model = Produto
    fields = ["nome","descricao","preco","categoria"]
    success_url = reverse_lazy("update_produto")

class ProdutoListView(ListView):
    model = Produto
    success_url = reverse_lazy("produto_list")


class ProdutoDeleteView(DeleteView):
    model = Produto
    success_url = reverse_lazy("produto_list")