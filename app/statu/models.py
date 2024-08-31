from django.db import models

# Create your models here.
class Status(models.Model):
    statu_id = models.AutoField(primary_key=True)
    statu_name = models.CharField(max_length=100, blank=False, null=False, unique=True)