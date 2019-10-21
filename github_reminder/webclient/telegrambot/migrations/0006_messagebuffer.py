# Generated by Django 2.2.4 on 2019-10-21 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telegrambot', '0005_auto_20191021_1428'),
    ]

    operations = [
        migrations.CreateModel(
            name='messageBuffer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('message', models.TextField(max_length=4096)),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-timestamp', '-updated'],
            },
        ),
    ]