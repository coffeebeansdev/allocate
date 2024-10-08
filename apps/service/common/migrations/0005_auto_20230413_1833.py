# Generated by Django 4.1.3 on 2023-03-14 09:17
from django.db import migrations
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType


def create_permission(apps, schema_editor):
    content_type = ContentType.objects.create(
        app_label='user_experience',
        model='edit_user_experience_permission',
    )
    Permission.objects.create(
        codename='can_edit_user_experience',
        name='Can edit user experience',
        content_type=content_type,
    )


def delete_permission(apps, schema_editor):
    Permission.objects.filter(codename='can_edit_user_experience').delete()


class Migration(migrations.Migration):
    dependencies = [
        ("common", "0004_auto_20230316_0858"),
    ]

    operations = [
        migrations.RunPython(create_permission, reverse_code=delete_permission),
    ]