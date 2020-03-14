# Generated by Django 3.0.2 on 2020-02-07 05:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('analyse', '0002_auto_20200206_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='p_app',
            field=models.BooleanField(default=False, null=True, verbose_name='Approval'),
        ),
        migrations.AlterField(
            model_name='package',
            name='p_det',
            field=models.TextField(blank=True, verbose_name='Additional Details'),
        ),
        migrations.AlterField(
            model_name='package',
            name='p_high',
            field=models.TextField(blank=True, verbose_name='Tour Highlights'),
        ),
        migrations.AlterField(
            model_name='package',
            name='p_img',
            field=models.FileField(upload_to='media/', verbose_name='Main Image'),
        ),
        migrations.AlterField(
            model_name='package',
            name='p_loc',
            field=models.CharField(max_length=300, verbose_name='Location'),
        ),
        migrations.AlterField(
            model_name='package',
            name='p_name',
            field=models.CharField(max_length=300, verbose_name='Name of Package'),
        ),
        migrations.AlterField(
            model_name='package',
            name='p_price',
            field=models.TextField(blank=True, verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='pckimg',
            name='p_img1',
            field=models.FileField(upload_to='media/', verbose_name='Image 1'),
        ),
        migrations.AlterField(
            model_name='pckimg',
            name='p_img2',
            field=models.FileField(upload_to='media/', verbose_name='Image 2'),
        ),
        migrations.AlterField(
            model_name='pckimg',
            name='p_img3',
            field=models.FileField(upload_to='media/', verbose_name='Image 3'),
        ),
        migrations.AlterField(
            model_name='pckimg',
            name='p_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='analyse.package', verbose_name='Package'),
        ),
    ]
