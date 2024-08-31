from django.db import models
from ..author.models import Authors
from ..genre.models import Gender

# Create your models here.
class Books(models.Model):
    book_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    author_id = models.ForeignKey(Authors, on_delete=models.CASCADE)
    publication_date = models.DateField()
    genre_id = models.ForeignKey(Gender, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=20)

    
    def __str__(self):
        return f"{self.title} {self.genre_id} {self.status}"