# Generated by Django 4.0.1 on 2023-05-28 03:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TipoEquipo',
            fields=[
                ('SK_TIPO_EQUIPO', models.AutoField(primary_key=True, serialize=False)),
                ('ST_TIPO_EQUIPO', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'db_table': 'tipo_equipo',
            },
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('SK_EQUIPO', models.AutoField(primary_key=True, serialize=False)),
                ('ST_NOMBRE_EQUIPO', models.CharField(max_length=50, unique=True)),
                ('ST_DESCRIPCION_EQUIPO', models.CharField(max_length=120)),
                ('SK_TIPO_EQUIPO', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Equipo.tipoequipo')),
            ],
            options={
                'db_table': 'equipo',
            },
        ),
    ]
