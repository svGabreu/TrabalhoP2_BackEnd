from django.db import models

class Categoria(models.Model):
    nome = models.CharField(verbose_name="Nome",max_length=100,null=False,blank=False)
    descricao = models.CharField(verbose_name="Descrição",max_length=100,null=False,blank=False)
    created_at = models.DateTimeField(verbose_name="Criado em",auto_now_add=True,null=False,blank=False)

class Produto(models.Model):
    nome = models.CharField(verbose_name="Nome",max_length=100,null=False,blank=False)
    descricao = models.CharField(verbose_name="Descrição",max_length=100,null=False,blank=False)
    preco = models.BigIntegerField(verbose_name="Preço",null=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="categoria")
    created_at = models.DateTimeField(verbose_name="Criado em",auto_now_add=True,null=False,blank=False)

#class Foto(models.Model):
#     url = models.URLField (max_length=200)