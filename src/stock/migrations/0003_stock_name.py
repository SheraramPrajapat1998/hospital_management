# Generated by Django 3.1.7 on 2021-04-29 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_stock_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='name',
            field=models.CharField(default=12, max_length=255),
            preserve_default=False,
        ),
    ]