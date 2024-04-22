# Generated by Django 4.2.11 on 2024-04-22 21:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id_categoria', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_categoria', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cif', models.CharField(max_length=10)),
                ('nombre_empresa', models.CharField(max_length=10)),
                ('direccion', models.CharField(max_length=50)),
                ('contacto', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_pedido', models.CharField(max_length=10)),
                ('fecha', models.DateField()),
                ('precio_total', models.IntegerField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresaDjango.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_producto', models.CharField(max_length=10)),
                ('nombre_producto', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=50)),
                ('precio_unidad', models.IntegerField()),
                ('modelo', models.CharField(max_length=50)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresaDjango.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='ProductoPedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresaDjango.pedido')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresaDjango.producto')),
            ],
        ),
        migrations.CreateModel(
            name='Componente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_componente', models.CharField(max_length=10)),
                ('nombre_componente', models.CharField(max_length=50)),
                ('marca', models.CharField(max_length=50)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresaDjango.producto')),
            ],
        ),
    ]
