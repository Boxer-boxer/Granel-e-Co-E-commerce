# Generated by Django 2.2.5 on 2019-09-24 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_auto_20190924_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtogranel',
            name='image',
            field=models.ImageField(upload_to='granel/catalog/static/catalog/img'),
        ),
    ]
