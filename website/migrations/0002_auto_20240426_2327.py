# Generated by Django 3.2.25 on 2024-04-26 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contant',
            new_name='Contact',
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ['created_date']},
        ),
    ]
