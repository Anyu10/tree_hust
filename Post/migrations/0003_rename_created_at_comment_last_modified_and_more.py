# Generated by Django 4.1 on 2022-11-05 05:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Post", "0002_remove_comment_return_to_comment_reply_to_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="comment", old_name="created_at", new_name="last_modified",
        ),
        migrations.RenameField(
            model_name="post", old_name="created_at", new_name="last_modified",
        ),
    ]