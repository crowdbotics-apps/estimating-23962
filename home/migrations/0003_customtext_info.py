# Generated by Django 2.2.17 on 2021-01-21 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_load_initial_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='customtext',
            name='info',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
