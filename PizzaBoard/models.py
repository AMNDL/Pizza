from django.db import models
from django.core.validators import MinValueValidator
from django_extensions.db.models import TimeStampedModel
from phone_field import PhoneField
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class Pizza(models.Model):
    name = models.CharField(verbose_name='Название', max_length=255)
    price = models.DecimalField(verbose_name='Цена (грн)', validators=[MinValueValidator(0)],
                                decimal_places=2, max_digits=5)
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    image = models.ImageField(verbose_name='Изображение', upload_to='images', null=True, blank=True)
    weight = models.PositiveIntegerField(verbose_name='Вес (г)', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пицца'
        verbose_name_plural = 'Пиццы'


class Order(TimeStampedModel):
    customer_name = models.CharField(verbose_name='Имя', max_length=50)
    delivery_time = models.DateTimeField(verbose_name='Время доставки', null=True, blank=True)
    delivery_address = models.TextField(verbose_name='Адрес доставки', null=True, blank=True)
    user_email = models.EmailField(verbose_name='Email пользователя', null=True, blank=True)
    user_phone = PhoneField(verbose_name='Телефон пользователя')
    price = models.DecimalField(verbose_name='Цена (грн)', validators=[MinValueValidator(0)],
                                decimal_places=2, max_digits=5, null=True, blank=True)
    pizzas = models.ManyToManyField('Pizza')

    def __str__(self):
        return f'Заказ номер {self.pk}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
