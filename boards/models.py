from django.db import models

# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=200, null=False)
    contents = models.TextField(null=False)
    file = models.FileField(upload_to='boards/')

    def __str__(self):
        return self.title
