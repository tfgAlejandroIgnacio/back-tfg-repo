from django.urls import path
from .views import CocineroSimple, CocineroComplejo

urlpatterns = [
    path('', CocineroSimple.as_view(), name="cocineros_simple"),
    path('<int:id>', CocineroComplejo.as_view(), name="cocineros_complejo")
]