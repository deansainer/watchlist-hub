# Generated by Django 4.2.4 on 2023-08-21 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizer_app', '0007_delete_deletedcontent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
