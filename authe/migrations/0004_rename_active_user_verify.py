# Generated by Django 4.0.2 on 2022-02-11 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authe', '0003_user_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='active',
            new_name='verify',
        ),
    ]
