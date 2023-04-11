from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(
        verbose_name='название',
        max_length=50,
        blank=False,
        null=False
    )
    
    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('app:request_list_filtered', kwargs={'pk':self.pk})

class ServiceRequest(models.Model):
    title = models.CharField(
        verbose_name='заголовок',
        max_length=100,
        blank=False,
    )
    description = models.TextField(
        verbose_name='описание',
        blank=True,
    )
    price_from = models.PositiveIntegerField(
        verbose_name='цена от',
        blank=False
    )
    price_to = models.PositiveIntegerField(
        verbose_name='цена до',
        blank=False
    )
    place = models.TextField(
        verbose_name='место',
        blank=True,
    )
    term = models.PositiveIntegerField()
    customer = models.ForeignKey(
        verbose_name='заказчик',
        blank=False,
        to=get_user_model(),
        related_name='service_requests',
        on_delete=models.CASCADE,
    )
    category = models.ForeignKey(
        verbose_name='категория',
        blank=False,
        to=Category,
        related_name='requests',
        on_delete=models.CASCADE,
    )
    
    def __str__(self) -> str:
        return f'{self.title} | {self.customer}'
    
    def clean(self) -> None:
        super().clean()
        if not self.price_from < self.price_to:
            raise ValidationError('Введите корректную сумму')
        
        if not self.customer.is_customer:
            raise ValidationError('Пользователь должен быть заказчиком')
        
    def get_absolute_url(self):
        return reverse('app:request_detail', kwargs={'pk':self.pk})
        
    def get_url_to_create_response(self):
        return reverse('app:response_create', kwargs={'pk':self.pk})
    
    def get_edit_url(self):
        return reverse('app:my_requests_edit', kwargs={'pk':self.pk})
    
    def get_delete_url(self):
        return reverse('app:my_requests_delete', kwargs={'pk':self.pk})

class ServiceResponse(models.Model):
    service_request = models.ForeignKey(
        verbose_name='запрос на услугу',
        blank=False,
        to=ServiceRequest,
        related_name='responses',
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        verbose_name='исполнитель',
        blank=False,
        to=get_user_model(),
        related_name='responses',
        on_delete=models.CASCADE,
    )
    text = models.TextField(
        verbose_name='текст',
        blank=True,
    )
    watched = models.BooleanField(
        verbose_name='просмотрено',
        blank=False,
        null=False,
        default=False,
    )
    
    def __str__(self):
        return f'{self.user} | {self.service_request.title}'
    
    def clean(self) -> None:
        super().clean()
        if self.user.is_customer:
            raise ValidationError('Пользователь должен быть исполнителем')
        
    def get_absolute_url(self):
        return reverse('app:response_detail', kwargs={'pk':self.pk})