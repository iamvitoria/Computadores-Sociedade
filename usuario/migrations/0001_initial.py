# Generated by Django 4.2.5 on 2024-05-15 16:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('nome', models.CharField(help_text='Nome do usuário', max_length=250, verbose_name='Nome')),
                ('idade', models.PositiveIntegerField(verbose_name='Idade')),
                ('email', models.EmailField(max_length=254, unique=True, validators=[django.core.validators.EmailValidator()], verbose_name='E-mail')),
                ('cpf', models.CharField(max_length=14, unique=True, verbose_name='CPF')),
                ('endereco', models.CharField(blank=True, max_length=255, verbose_name='Endereço')),
                ('numero', models.CharField(blank=True, max_length=10, verbose_name='Número')),
                ('complemento', models.CharField(blank=True, max_length=255, verbose_name='Complemento')),
                ('bairro', models.CharField(blank=True, max_length=100, verbose_name='Bairro')),
                ('cidade', models.CharField(blank=True, max_length=100, verbose_name='Cidade')),
                ('estado', models.CharField(blank=True, max_length=100, verbose_name='Estado')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
