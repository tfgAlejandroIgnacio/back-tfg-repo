# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class DetallesPedido(models.Model):
    id_producto = models.ForeignKey('producto.Producto', models.DO_NOTHING, db_column='id_producto')
    id_pedido = models.ForeignKey('pedido.Pedido', models.DO_NOTHING, db_column='id_pedido')
    cantidad = models.IntegerField()
    precio = models.FloatField()
    fecha_entrega = models.DateField()

    class Meta:
        db_table = 'detalles_pedido'
