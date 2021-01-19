from django.db import models

class Todo(models.Model):
    name = models.CharField(max_length=100)
    due_date = models.DateField()

    ### To show name in admin list
    def __str__(self):
        return self.name