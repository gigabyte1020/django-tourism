# Generated by Django 3.0.2 on 2020-02-10 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_auto_20200210_1051'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='app',
            field=models.BooleanField(null=True, verbose_name='Approval'),
        ),
    ]
