# Generated by Django 3.0.2 on 2020-02-12 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_auto_20200210_1427'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='num',
            field=models.IntegerField(blank=True, default=1),
        ),
        migrations.AlterField(
            model_name='cart',
            name='date',
            field=models.DateField(blank=True),
        ),
    ]