# Generated by Django 3.2.8 on 2022-06-30 01:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agendacontactos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='libro',
            old_name='description',
            new_name='descripcion',
        ),
    ]
