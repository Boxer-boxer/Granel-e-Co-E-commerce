# Generated by Django 2.2.5 on 2019-09-24 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20190924_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtogranel',
            name='image',
            field=models.ImageField(upload_to='static/catalog/img'),
        ),
    ]
