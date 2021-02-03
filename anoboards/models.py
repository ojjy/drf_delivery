from django.db import models

# Create your models here.


class AnonymBoard(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.content[:128]
