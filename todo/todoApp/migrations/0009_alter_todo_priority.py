# Generated by Django 5.0.2 on 2024-02-12 15:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("todoApp", "0008_alter_todo_priority"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todo",
            name="priority",
            field=models.CharField(
                choices=[("🟥", "High"), ("🟧", "Medium"), ("🟩", "Low")], max_length=2
            ),
        ),
    ]