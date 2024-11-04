from django.contrib import admin
from django.urls import path
from ecommerce.views import ecommerce_list
from ecommerce.views import CriarCategoria, CriarProduto, UpdateProduto, ProdutoListView, ProdutoDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", ecommerce_list),
    path("",ProdutoListView.as_view(), name="produto_list"),
    path("create",CriarCategoria.as_view(), name="criar_categoria"),
    path("create",CriarProduto.as_view(),name="criar_produto"),
    path("update/<int:pk>",UpdateProduto.as_view(),name="update_produto"),
    path("delete",ProdutoDeleteView.as_view(),name="produto_delete"),

]