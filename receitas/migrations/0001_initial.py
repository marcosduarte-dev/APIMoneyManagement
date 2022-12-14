# Generated by Django 4.1.3 on 2022-12-12 22:18

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Receitas",
            fields=[
                (
                    "id_receita",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("id_conta", models.CharField(max_length=50)),
                ("valor", models.FloatField()),
                ("data_lancamento", models.DateField()),
                ("data_receita", models.DateField()),
            ],
        ),
    ]
