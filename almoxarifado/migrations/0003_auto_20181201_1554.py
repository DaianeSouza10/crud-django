# Generated by Django 2.1.3 on 2018-12-01 18:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('almoxarifado', '0002_auto_20181126_1515'),
    ]

    operations = [
        migrations.RenameField(
            model_name='almoxarifado',
            old_name='description',
            new_name='descrição',
        ),
        migrations.RenameField(
            model_name='almoxarifado',
            old_name='name',
            new_name='nome',
        ),
        migrations.RenameField(
            model_name='almoxarifado',
            old_name='quantity',
            new_name='quantidade',
        ),
        migrations.RenameField(
            model_name='almoxarifado',
            old_name='user',
            new_name='usuário',
        ),
    ]