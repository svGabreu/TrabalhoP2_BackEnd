from django.contrib import admin
from django.urls import path
from ecommerce.views import CriarCategoria, CriarProduto, UpdateProduto, ProdutoListView, ProdutoDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",ProdutoListView.as_view()),
    path("create",CriarCategoria.as_view()),
    path("create",CriarProduto.as_view()),
    path("update",UpdateProduto.as_view()),
    path("delete",ProdutoDeleteView.as_view()),

]
