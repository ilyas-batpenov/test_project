# Generated by Django 4.0.4 on 2022-04-11 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='update_counter',
            field=models.IntegerField(default=0, verbose_name='Update counter'),
        ),
    ]
