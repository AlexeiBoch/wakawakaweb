# Generated by Django 2.2 on 2023-04-10 10:28

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=256, unique=True, verbose_name='электронная почта')),
                ('first_name', models.CharField(max_length=50, verbose_name='имя')),
                ('last_name', models.CharField(max_length=50, verbose_name='фамилия')),
                ('patronymic', models.CharField(blank=True, max_length=50, verbose_name='отчество')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
                ('description', models.TextField(verbose_name='описание')),
                ('customer', models.BooleanField(default=False, verbose_name='заказчик')),
                ('staff', models.BooleanField(default=False, verbose_name='персонал')),
                ('admin', models.BooleanField(default=False, verbose_name='администратор')),
            ],
            options={
                'verbose_name': 'пользователь',
                'verbose_name_plural': 'пользователи',
            },
        ),
    ]
