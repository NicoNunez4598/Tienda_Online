# Generated by Django 5.0.6 on 2024-08-26 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=20)),
                ('Seccion', models.CharField(max_length=30)),
                ('Precio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=40)),
                ('Direccion', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=254)),
                ('Telefono', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Pedidos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Numero', models.IntegerField()),
                ('Fecha', models.DateField()),
                ('Entregado', models.BooleanField()),
            ],
        ),
    ]
