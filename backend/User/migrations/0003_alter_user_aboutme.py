# Generated by Django 4.1 on 2022-11-08 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='aboutme',
            field=models.CharField(default='这个用户啥也没说...', max_length=150),
        ),
    ]
