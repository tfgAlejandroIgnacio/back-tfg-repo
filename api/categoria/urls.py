from django.urls import path
from .views import CategoriaSimple, CategoriaConId

urlpatterns = [
    path('', CategoriaSimple.as_view(), name="categoria_simple"),
    path('<int:id>', CategoriaConId.as_view(), name="categoria_con_id")
]