# Generated by Django 4.1.7 on 2023-07-14 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_library_created_time_library_updated_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='library',
            name='updated_time',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]