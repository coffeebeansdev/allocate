# Generated by Django 4.1.3 on 2022-12-12 05:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'permissions': [('mark_client_dormant', 'Can mark client dormant'), ('client_account_manager', 'Can be client account manager')]},
        ),
    ]
