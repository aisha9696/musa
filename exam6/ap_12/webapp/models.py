from django.db import models


class Record(models.Model):
    ACTIVE = "active"
    BLOCKED = "blocked"
    CHOICES = [
        (ACTIVE, "active"),
        (BLOCKED, "blocked"),
    ]
    author = models.CharField(
        max_length=40, null=False, blank=False, verbose_name='Автор',
    )
    email = models.EmailField(
        max_length=40, null=False, blank=False, verbose_name='Почта',
    )
    text = models.TextField(
        null=False, blank=False, verbose_name='Текст',
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    status = models.CharField(max_length=7, null=False, choices=CHOICES, default=ACTIVE, verbose_name='Статус')
