from django.db import models

class TodoModel(models.Model):
    title = models.TextField(blank=False)
    isCompleted = models.BooleanField(default=False)
    add_date = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.title
    