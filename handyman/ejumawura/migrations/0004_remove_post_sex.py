# Generated by Django 4.2.10 on 2024-06-22 02:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("ejumawura", "0003_remove_post_community"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="sex",
        ),
    ]