# Generated by Django 4.0.3 on 2022-04-08 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0005_rename_addresses_address_rename_clients_client_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='last_name',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
