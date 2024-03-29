# Generated by Django 5.0.1 on 2024-02-02 21:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0003_usuario_date_joined_usuario_is_active_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='nombre_usuario',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='rol',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sistema.rol'),
        ),
    ]
