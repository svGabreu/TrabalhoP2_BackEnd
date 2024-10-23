from django.contrib import admin
from django.urls import path
from ecommerce.views import ecommerce_app

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",ecommerce_app),
]
