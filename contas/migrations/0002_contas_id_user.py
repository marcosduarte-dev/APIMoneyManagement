# Generated by Django 4.1.3 on 2022-12-09 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contas", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="contas",
            name="id_user",
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
