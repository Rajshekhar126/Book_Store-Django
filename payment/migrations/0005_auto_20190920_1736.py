# Generated by Django 2.2.1 on 2019-09-20 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0004_auto_20190920_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='card_no',
            field=models.CharField(max_length=16),
        ),
    ]
