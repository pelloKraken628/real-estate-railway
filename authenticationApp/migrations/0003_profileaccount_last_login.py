# Generated by Django 4.0.5 on 2022-06-23 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticationApp', '0002_profileaccount_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='profileaccount',
            name='last_login',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]
