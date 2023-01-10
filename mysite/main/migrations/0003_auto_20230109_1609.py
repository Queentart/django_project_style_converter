# Generated by Django 3.2.5 on 2023-01-09 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_file_upload_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='file_upload',
            old_name='name',
            new_name='filename',
        ),
        migrations.AlterField(
            model_name='file_upload',
            name='data',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
