# Generated by Django 5.0 on 2024-02-11 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='ip_address',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]