# Generated by Django 2.2.4 on 2019-10-16 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telegrambot', '0005_auto_20191016_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messagebuffer',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='messagelogs',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
    ]