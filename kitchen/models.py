from django.db import models
from django.utils.translation import gettext_lazy as _


class Recipe(models.Model):
    class RecipeType(models.TextChoices):
        breakfast = 'Завтрак', _('Завтрак')
        lunch = 'Полдник', _('Полдник')
        dinner = 'Обед', _('Обед')
        supper = 'Ужин', _('Ужин')
        snack = 'Закуска', _('Закуска')

    name = models.CharField(max_length=50, verbose_name='Название')
    author = models.CharField(max_length=50, verbose_name='Автор')
    type = models.CharField(
        max_length=7,
        choices=RecipeType.choices,
        default=RecipeType.breakfast,
        verbose_name='Тип',
    )
    description = models.TextField(verbose_name='Описание')
    ingredients = models.TextField(verbose_name='Ингредиенты')
    country = models.CharField(max_length=50, verbose_name='Страна')

    def __str__(self):
        return self.name
