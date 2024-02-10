from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100, verbose_name='Напишите хэштег', default='#')

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название продукта')
    description = models.TextField(blank=True, verbose_name='Описание продукта')
    price = models.PositiveIntegerField(verbose_name='Укажите цену продукта')
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
