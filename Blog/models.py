from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail

NULLABLE = {'blank': True, 'null': True}


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='заголовок')
    slug = models.CharField(max_length=150, unique=True, verbose_name='slug', **NULLABLE)
    description = models.TextField(**NULLABLE, verbose_name='содержимое')
    image = models.ImageField(upload_to='image/', verbose_name='превью(изображение)', **NULLABLE)
    date = models.DateField(**NULLABLE, verbose_name='дата создания')
    is_active = models.BooleanField(default=True, verbose_name='признак публикации')
    count_view = models.IntegerField(default=0, verbose_name='количество просмотров')

    def __str__(self):
        return f'{self.title} {self.slug}'

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'



