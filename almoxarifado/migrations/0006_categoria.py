# Generated by Django 2.1.3 on 2018-12-03 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almoxarifado', '0005_auto_20181203_0830'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id_categoria', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('nome_categoria', models.CharField(max_length=100)),
            ],
        ),
    ]