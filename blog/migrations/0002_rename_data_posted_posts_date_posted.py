# Generated by Django 4.1.7 on 2024-01-21 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posts',
            old_name='data_posted',
            new_name='date_posted',
        ),
    ]