from django.contrib.auth.models import User
from django.db import models

class Perfil(models.Model):
    user = models.OneToOneField(User, null=False, related_name="%(class)s")
    cedula = models.CharField(max_length=32)
    id = models.AutoField(primary_key=True)
    class Meta:
        abstract = True



# Create your models here.
