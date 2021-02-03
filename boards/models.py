from django.db import models

# Create your models here.


class Board(models.Model):
    title = models.CharField(max_length=200, verbose_name="title")
    author = models.CharField(max_length=200, verbose_name="author")
    pub_date = models.DateTimeField('date published', auto_now=True)
    content = models.TextField(verbose_name="content")

    def __str__(self):
        return self.title

    def summary(self):
        return self.content[:128]


class Comment(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE, null=True, related_name='comments')
    comment_date = models.DateTimeField(auto_now_add=True)
    comment_body = models.CharField(max_length=1024)
    comment_user = models.CharField(max_length=128)

    def __str__(self):
        return self.pk + ": "+self.comment_body[:16]

    def summary(self):
        return self.comment_body[:128]

    class Meta:
        ordering=["comment_date"]
