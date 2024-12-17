from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from accounts.models import User
from django.contrib.auth import get_user_model


class Product(models.Model):
    CHOICES = [
        ("Components", "Components"),
        ("Laptops", "Laptops"),
        ("Smartphones", "Smartphones"),
        ("Periphery", "Periphery"),
    ]
    name = models.CharField(null=False, blank=False, max_length=40, verbose_name="Название")
    category = models.CharField(max_length=20, choices=CHOICES, verbose_name="Категория")
    description = models.TextField(max_length=400, null=True, blank=True, verbose_name="Описание")
    picture = models.ImageField(null=True, blank=True, upload_to='pictures', verbose_name="Картинка")

    def __str__(self):
        return self.name


class Review(models.Model):
    author = models.ForeignKey(get_user_model(), related_name='reviews', on_delete=models.CASCADE, null=False, blank=False, verbose_name='Автор')
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE, null=False, blank=False, verbose_name='Товар')
    text = models.TextField(null=False, blank=False, max_length=800, verbose_name='Текст отзыва')
    grade = models.IntegerField(null=False, blank=False, validators=[MinValueValidator(1), MaxValueValidator(5)],
                                verbose_name='Оценка')
