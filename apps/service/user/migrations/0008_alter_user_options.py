# Generated by Django 4.1.3 on 2023-01-05 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_alter_leaveplans_from_date_alter_leaveplans_to_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'permissions': [('login', 'Can login'), ('search_talent', 'Can search talent')]},
        ),
    ]
