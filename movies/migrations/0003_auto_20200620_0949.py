# Generated by Django 3.0.7 on 2020-06-20 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20200619_1610'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating',
            old_name='starts',
            new_name='stars',
        ),
    ]
