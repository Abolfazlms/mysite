# Generated by Django 5.0.6 on 2024-05-31 20:02

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0009_comments_post"),
    ]

    operations = [
        migrations.RenameField(
            model_name="comments",
            old_name="approve",
            new_name="approved",
        ),
    ]
