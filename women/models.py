from django.db import models


class Women(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)  # blank=True - не обязательно заполнять
    time_create = models.DateTimeField(auto_now_add=True)  # auto_now_add - заполняется только при создании
    time_update = models.DateTimeField(auto_now=True)  # auto_now - меняется дата при каждом изменении
    is_published = models.BooleanField(default=True)  # default=True - дефолтное значение True

    def __str__(self):
        return self.title
