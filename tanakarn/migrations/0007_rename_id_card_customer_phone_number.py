# Generated by Django 5.0 on 2024-01-17 04:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tanakarn', '0006_rename_phone_number_customer_id_card'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='id_card',
            new_name='phone_number',
        ),
    ]