# Generated by Django 4.1.3 on 2022-12-17 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppForm', '0006_alter_persona_fecha_nacimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.FloatField(),
        ),
    ]