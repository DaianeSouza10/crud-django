# Generated by Django 2.1.3 on 2018-12-03 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('almoxarifado', '0007_auto_20181203_0848'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categoria',
            old_name='id_categoria',
            new_name='id',
        ),
    ]
