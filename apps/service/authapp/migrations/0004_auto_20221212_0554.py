# Generated by Django 4.1.3 on 2022-12-12 05:54

from django.contrib.contenttypes.models import ContentType
from django.db import migrations

from authapp.constants import RoleKeys
from authapp.permissions import assign_permissions, revoke_permissions


def get_group_permission_map(content_type):
    group_permission_map = {
        RoleKeys.ACCOUNT_MANAGER: {
            'content_type': content_type,
            'codenames': ['client_account_manager']
        }
    }
    return group_permission_map


def assign_group_permissions(apps, schema_editor):
    Client = apps.get_model('client', 'Client')
    content_type = ContentType.objects.get_for_model(Client)
    group_permission_map = get_group_permission_map(content_type)
    assign_permissions(group_permission_map)


def revoke_group_permissions(apps, schema_editor):
    Client = apps.get_model('client', 'Client')
    content_type = ContentType.objects.get_for_model(Client)
    group_permission_map = get_group_permission_map(content_type)
    revoke_permissions(group_permission_map)


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0003_auto_20221209_1020'),
        ('client', '0002_alter_client_options')
    ]

    operations = [
        migrations.RunPython(assign_group_permissions, reverse_code=revoke_group_permissions)
    ]
