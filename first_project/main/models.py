from django.db import models


class Task(models.Model):
    title = models.CharField('Title', max_length=100)
    text = models.TextField('Text')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачі'
