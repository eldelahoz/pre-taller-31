from django.db import models
from ..author.models import Authors
from ..genre.models import Gender
from ..statu.models import Status

# Create your models here.
class Books(models.Model):
    book_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    author_id = models.ForeignKey(Authors, on_delete=models.CASCADE)
    publication_date = models.DateField()
    genre_id = models.ForeignKey(Gender, on_delete=models.SET_NULL, null=True)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)

    
    def __str__(self):
        return f"{self.title} {self.genre_id} {self.status}"