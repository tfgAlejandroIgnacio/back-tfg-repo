# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.hashers import make_password


class Cocinero(models.Model):
    nombre = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=300)
    correo = models.CharField(max_length=300)
    contraseña = models.CharField(max_length=200)

    class Meta:
        db_table = 'cocinero'

    def save(self, *args, **kwargs):
        # Si la contraseña ya está hasheada, no la vuelvas a hashear
        if not self.contraseña.startswith(('pbkdf2_', 'argon2$', 'bcrypt$', 'scrypt$')):
            self.contraseña = make_password(self.contraseña)
        super().save(*args, **kwargs)    
