# Generated by Django 4.0.1 on 2023-06-11 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Equipo', '0004_equipo_st_img_equipo_alter_equipo_sk_tipo_equipo_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='equipo',
            old_name='SK_TIPO_EQUIPO',
            new_name='FK_TIPO_EQUIPO',
        ),
        migrations.AlterField(
            model_name='equipo',
            name='ST_NOMBRE_EQUIPO',
            field=models.CharField(error_messages={'unique': 'El nombre de equipo ingresado ya existe en el sistema. Por favor, ingrese otro nombre.'}, max_length=50, unique=True, verbose_name='Nombre'),
        ),
    ]
