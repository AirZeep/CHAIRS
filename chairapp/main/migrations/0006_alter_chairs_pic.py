# Generated by Django 4.1.7 on 2023-03-11 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_chairs_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chairs',
            name='pic',
            field=models.ImageField(upload_to='static/main/img/', verbose_name='Picture'),
        ),
    ]