from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, verbose_name="Название")
    year_of_publishing = models.CharField(max_length=40, null=False, blank=False, verbose_name="Год публикации")
    author = models.CharField
    author = models.ForeignKey(
        'webapp.Author',
        related_name='book',
        on_delete=models.CASCADE,
        verbose_name='Автор')
    description = models.TextField(max_length=200, null=True, blank=True, verbose_name="Описание")
    genre = models.ManyToManyField(
        'webapp.Genre',
        related_name='book',
        verbose_name='Типы')


class Author(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, verbose_name="Имя автора")
    dates_of_life = models.CharField(max_length=40, null=True, blank=True, verbose_name="Даты жизни")
    biography = models.TextField(max_length=400, null=False, blank=False, verbose_name="Биография")

    def __str__(self):
        return f'{self.name}'


class Genre(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, verbose_name="Название")

    def __str__(self):
        return f'{self.name}'
