# Generated by Django 5.0.6 on 2024-06-04 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logistic', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stock',
            old_name='address',
            new_name='adress',
        ),
    ]
