# Generated by Django 4.1.3 on 2022-12-17 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppForm', '0003_alter_persona_dni'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='fecha_nacimiento',
            field=models.DateTimeField(),
        ),
    ]
