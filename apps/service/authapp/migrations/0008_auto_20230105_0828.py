# Generated by Django 4.1.3 on 2023-01-05 08:28

from django.contrib.contenttypes.models import ContentType
from django.db import migrations

from authapp.constants import RoleKeys
from authapp.permissions import assign_permissions, revoke_permissions


def get_group_permission_map(content_type):
    group_permission_map = {
        RoleKeys.ADMIN: {
            'content_type': content_type,
            'codenames': ['search_talent']
        },
        RoleKeys.ACCOUNT_MANAGER: {
            'content_type': content_type,
            'codenames': ['search_talent']
        }
    }
    return group_permission_map


def assign_group_permissions(apps, schema_editor):
    User = apps.get_model('user', 'User')
    content_type = ContentType.objects.get_for_model(User)
    group_permission_map = get_group_permission_map(content_type)
    assign_permissions(group_permission_map)


def revoke_group_permissions(apps, schema_editor):
    User = apps.get_model('user', 'User')
    content_type = ContentType.objects.get_for_model(User)
    group_permission_map = get_group_permission_map(content_type)
    revoke_permissions(group_permission_map)


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0007_auto_20230102_1058'),
        ('user', '0008_alter_user_options')
    ]

    operations = [
        migrations.RunPython(assign_group_permissions, reverse_code=revoke_group_permissions)
    ]
