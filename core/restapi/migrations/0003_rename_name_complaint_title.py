# Generated by Django 4.2.2 on 2023-06-20 16:16

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("restapi", "0002_remove_comment_updated_at"),
    ]

    operations = [
        migrations.RenameField(
            model_name="complaint",
            old_name="name",
            new_name="title",
        ),
    ]
