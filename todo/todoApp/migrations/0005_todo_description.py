# Generated by Django 5.0.2 on 2024-02-12 13:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("todoApp", "0004_todo_delete_signup"),
    ]

    operations = [
        migrations.AddField(
            model_name="todo",
            name="description",
            field=models.CharField(default="", max_length=50),
        ),
    ]