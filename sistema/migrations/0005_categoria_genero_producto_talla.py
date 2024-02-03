# Generated by Django 5.0.1 on 2024-02-02 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0004_alter_usuario_nombre_usuario_alter_usuario_rol'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='genero',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino'), ('U', 'Unisex'), ('N', 'No Especificado')], default='N', max_length=1),
        ),
        migrations.AddField(
            model_name='producto',
            name='talla',
            field=models.CharField(choices=[('XS', 'Extra Small'), ('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Extra Large'), ('XXL', 'Double Extra Large'), ('XXXL', 'Triple Extra Large'), ('XXXXL', 'Quadruple Extra Large')], default='M', max_length=5),
        ),
    ]
