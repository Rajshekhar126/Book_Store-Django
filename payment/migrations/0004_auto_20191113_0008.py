# Generated by Django 2.2.1 on 2019-11-13 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0003_auto_20191112_2344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='card_holder_name',
            field=models.CharField(default=' ', max_length=60),
        ),
        migrations.AlterField(
            model_name='payment',
            name='card_no',
            field=models.CharField(default=' ', max_length=21),
        ),
    ]