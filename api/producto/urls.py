from django.urls import path
from .views import ProductoSimple, ProductoConId

urlpatterns = [
    path('', ProductoSimple.as_view(), name="producto_simple"),
    path('<int:id>', ProductoConId.as_view(), name="producto_con_id")
]