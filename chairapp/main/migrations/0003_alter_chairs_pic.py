# Generated by Django 4.1.7 on 2023-03-08 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_chairs_options_alter_chairs_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chairs',
            name='pic',
            field=models.ImageField(upload_to='chairapp/main/static/main/img', verbose_name='Picture'),
        ),
    ]
