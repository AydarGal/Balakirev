from django.db import models
from django.urls import reverse


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Women.Status.PUBLISHED)


class Women(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)  # unique - уникальное поле, db_index - индексируемое, чтобы быстрее статьи выбирались из бд
    content = models.TextField(blank=True)  # blank=True - не обязательно заполнять
    time_create = models.DateTimeField(auto_now_add=True)  # auto_now_add - заполняется только при создании
    time_update = models.DateTimeField(auto_now=True)  # auto_now - меняется дата при каждом изменении
    is_published = models.BooleanField(choices=Status.choices, default=Status.DRAFT)  # default=True - дефолтное значение True

    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-time_create']
        indexes = [
            models.Index(fields=['-time_create'])
        ]

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})
