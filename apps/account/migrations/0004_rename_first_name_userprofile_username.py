# Generated by Django 4.0.6 on 2022-08-08 21:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_userprofile_is_staff'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='first_name',
            new_name='username',
        ),
    ]