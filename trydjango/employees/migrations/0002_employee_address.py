# Generated by Django 3.2 on 2021-04-30 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='address',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
