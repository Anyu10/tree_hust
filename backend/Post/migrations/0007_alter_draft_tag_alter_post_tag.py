# Generated by Django 4.1 on 2022-11-26 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Post", "0006_alter_browser_history_browser_time_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="draft",
            name="tag",
            field=models.CharField(
                choices=[
                    ("1", "life is meaningless"),
                    ("2", "I am a procrastinator"),
                    ("3", "want to die"),
                    ("4", "venomous!"),
                    ("5", "I am a piece of shit"),
                    ("6", "I am the black sheep"),
                ],
                default="s",
                max_length=30,
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="tag",
            field=models.CharField(
                choices=[
                    ("1", "life is meaningless"),
                    ("2", "I am a procrastinator"),
                    ("3", "want to die"),
                    ("4", "venomous!"),
                    ("5", "I am a piece of shit"),
                    ("6", "I am the black sheep"),
                ],
                default="s",
                max_length=30,
            ),
        ),
    ]
