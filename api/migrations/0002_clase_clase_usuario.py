# Generated by Django 4.2.7 on 2023-11-24 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Clase",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("asignatura", models.CharField(max_length=100)),
                ("fecha", models.DateField()),
                ("hora", models.TimeField()),
                ("carrera", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Clase_Usuario",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("id_clase", models.IntegerField()),
                ("id_usuario", models.IntegerField()),
            ],
        ),
    ]
