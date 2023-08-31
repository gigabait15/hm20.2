from django.db import models
from config import settings

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(**NULLABLE, verbose_name='описание')

    is_publish = models.BooleanField(default=True, verbose_name='опубликовано')
    slug = models.CharField(max_length=150, verbose_name='slug', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(**NULLABLE, verbose_name='описание')
    image = models.ImageField(upload_to='image/', verbose_name='изображение ', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    price = models.IntegerField(**NULLABLE, verbose_name='цена за покупку')
    date_burn = models.DateField(**NULLABLE, verbose_name='дата создания')
    date = models.DateField(**NULLABLE, verbose_name='дата последнего изменения')

    is_active = models.BooleanField(default=True, verbose_name='в наличии')
    views_count = models.IntegerField(default=0, verbose_name='просмотры')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f'{self.name} {self.price}({self.description})'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Feedback(models.Model):
    name = models.CharField(max_length=100, verbose_name='name')
    email = models.EmailField(verbose_name='email')
    message = models.TextField(verbose_name='message')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='date')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')
    number_version = models.IntegerField(**NULLABLE, verbose_name='номер версии')
    name_version = models.CharField(max_length=100, verbose_name='название версии')
    active_version = models.BooleanField(default=True, verbose_name='признак текущей версии')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'