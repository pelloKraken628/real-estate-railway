# Generated by Django 3.2.6 on 2022-07-21 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticationApp', '0006_inboxmessages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inboxmessages',
            name='subject',
            field=models.CharField(choices=[('Bug problem', 'Bug problem'), ('partnership', 'partnership'), ('Just Saying Hello', 'Just Saying Hello')], default='Bug problem', max_length=50),
        ),
    ]