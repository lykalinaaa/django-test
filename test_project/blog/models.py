from django.db import models

class Post(models.Model):
    title = models.CharField(blank=False)
    text = models.CharField(blank=False)
    image = models.CharField(default="")
    category = models.CharField(default="Без категории")
    created_at = models.CharField(default="Нет данных")
    read_time = models.CharField(default="Нет данных")
    comments = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.title} \n {self.text}'
