# Generated by Django 5.1 on 2024-09-08 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0006_alter_registration_options_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='registration',
            unique_together={('roll_no', 'year')},
        ),
    ]
