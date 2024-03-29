# Generated by Django 5.0.3 on 2024-03-27 23:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("aplicacion4", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Consola",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=40)),
                ("año", models.CharField(max_length=40)),
                ("estado", models.CharField(max_length=40)),
                ("stock", models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name="Estudiante",
        ),
        migrations.AlterField(
            model_name="profesor",
            name="apellido",
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name="profesor",
            name="nombre",
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name="profesor",
            name="profesion",
            field=models.CharField(max_length=50),
        ),
    ]
