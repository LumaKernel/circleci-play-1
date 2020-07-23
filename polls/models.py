from django.db import models

class Question(models.Model):
    desc = models.TextField()

    def __str__(self):
        return self.desc
