from django.db import models

class Gender(models.Model):
    gender_id = models.AutoField(primary_key = True)
    gender_name = models.CharField(max_length = 30)

    def __str__(self):
        return f'{self.gender_name}'
