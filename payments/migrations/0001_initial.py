# Generated by Django 2.2.5 on 2019-09-25 10:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(default='code_order', max_length=100)),
                ('nome_completo', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('rua', models.CharField(max_length=300)),
                ('numero', models.CharField(max_length=300)),
                ('andar', models.IntegerField(blank=True, null=True)),
                ('localidade', models.CharField(default='', max_length=60)),
                ('distrito', models.CharField(choices=[('Aveiro', 'Aveiro'), ('Beja', 'Beja'), ('Braga', 'Braga'), ('Bragança', 'Bragança'), ('Castelo Branco', 'Castelo Branco'), ('Coimbra', 'Coimbra'), ('Évora', 'Évora'), ('Faro', 'Faro'), ('Guarda', 'Guarda'), ('Leiria', 'Leiria'), ('Lisboa', 'Lisboa'), ('Portalegre', 'Portalegre'), ('Porto', 'Porto'), ('Santarém', 'Santarém'), ('Setúbal', 'Setúbal'), ('Viana do Castelo', 'Viana do Castelo'), ('Vila Real', 'Vila Real'), ('Viseu', 'Viseu'), ('Ilha da Madeira', 'Ilha da Madeira'), ('Ilha de Porto Santo', 'Ilha de Porto Santo'), ('Ilha de Santa Maria', 'Ilha de Santa Maria'), ('Ilha de São Miguel', 'Ilha de São Miguel'), ('Ilha Terceira', 'Ilha Terceira'), ('Ilha da Graciosa', 'Ilha da Graciosa'), ('Ilha de São Jorge', 'Ilha de São Jorge'), ('Ilha do Pico', 'Ilha do Pico'), ('Ilha do Faial', 'Ilha do Faial'), ('Ilha das Flores', 'Ilha das Flores'), ('Ilha do Corvo', 'Ilha do Corvo')], default='', max_length=30)),
                ('morada', models.IntegerField(blank=True, default=0, null=True)),
                ('codigo_postal_1', models.IntegerField(blank=True, default=1000, null=True)),
                ('codigo_postal_2', models.IntegerField(blank=True, default=100, null=True)),
                ('items', models.CharField(default='', max_length=500)),
                ('total', models.IntegerField(blank=True, null=True)),
                ('is_ordered', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(default='', max_length=100)),
                ('cart', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.Cart')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
