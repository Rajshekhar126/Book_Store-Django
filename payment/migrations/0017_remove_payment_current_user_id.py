# Generated by Django 2.2.1 on 2019-10-14 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0016_payment_current_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='current_user_id',
        ),
    ]