# Generated by Django 3.0.2 on 2020-02-08 11:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('analyse', '0006_auto_20200207_1637'),
        ('home', '0013_auto_20200207_1124'),
    ]

    operations = [
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.TextField(blank=True)),
                ('status', models.BooleanField(default=False, null=True)),
                ('guide', models.TextField(blank=True)),
                ('pck', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='analyse.package')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
