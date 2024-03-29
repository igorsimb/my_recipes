# Generated by Django 3.2.4 on 2021-06-14 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kitchen', '0003_remove_recipe_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='name',
            field=models.CharField(default='', max_length=50, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='author',
            field=models.CharField(max_length=50, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='country',
            field=models.CharField(max_length=50, verbose_name='Страна'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.TextField(verbose_name='Ингредиенты'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='type',
            field=models.CharField(choices=[('Завтрак', 'Завтрак'), ('Полдник', 'Полдник'), ('Обед', 'Обед'), ('Ужин', 'Ужин'), ('Закуска', 'Закуска')], default='Завтрак', max_length=7, verbose_name='Тип'),
        ),
    ]
