# Generated by Django 2.2.5 on 2019-09-24 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20190924_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtogranel',
            name='image',
            field=models.ImageField(upload_to='static/catalog/img'),
        ),
    ]
