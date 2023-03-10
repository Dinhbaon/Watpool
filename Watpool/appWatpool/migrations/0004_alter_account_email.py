# Generated by Django 4.1.7 on 2023-02-22 02:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appWatpool', '0003_alter_account_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='email',
            field=models.EmailField(max_length=60, unique=True, validators=[django.core.validators.EmailValidator(allowlist=['uwaterloo.ca'], message='Use @uwaterloo.ca email')], verbose_name='email'),
        ),
    ]
