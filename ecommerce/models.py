from django.db import models

class Categoria(models.Model):
    id = models.IntegerField(auto_created=True,primary_key=True)
    nome_categoria = models.CharField(max_length=100,null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True,null=False,blank=False)
    descricao_categoria = models.CharField(max_length=100,null=False,blank=False)

class Produto(models.Model):
    id = models.IntegerField(auto_created=True,primary_key=True)
    nome_produto = models.CharField(max_length=100,null=False,blank=False)
    descricao_produto = models.CharField(max_length=100,null=False,blank=False)
    preco = models.BigIntegerField(max_length=10,null=False)
    categoria = models.ForeignKey("Categoria", on_delete=models.CASCADE)

class Foto(models.Model):
    id = models.IntegerField(auto_created=True,primary_key=True)
    url = models.URLField (max_length=200)
    produto = models.ForeignKey("Produto",on_delete=models.CASCADE)