# Generated by Django 4.2.7 on 2023-11-24 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Usuario",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("nombre", models.CharField(max_length=100)),
                ("apellido", models.CharField(max_length=100)),
                ("correo", models.CharField(max_length=100)),
                ("contrasena", models.CharField(max_length=100)),
                ("rol", models.CharField(max_length=100)),
            ],
        ),
    ]
