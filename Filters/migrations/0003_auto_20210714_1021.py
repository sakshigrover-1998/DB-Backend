# Generated by Django 3.2.4 on 2021-07-14 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Filters', '0002_alter_filterdata_cob_dt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filterdata',
            name='book_name',
            field=models.CharField(default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='filterdata',
            name='business_line',
            field=models.CharField(default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='filterdata',
            name='cob_dt',
            field=models.DateField(default='2000-01-01', null=True),
        ),
        migrations.AlterField(
            model_name='filterdata',
            name='filter_component',
            field=models.CharField(default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='filterdata',
            name='filter_description',
            field=models.CharField(default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='filterdata',
            name='filter_name',
            field=models.CharField(default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='filterdata',
            name='legal_entity',
            field=models.CharField(default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='filterdata',
            name='profit_center',
            field=models.CharField(default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='filterdata',
            name='region',
            field=models.CharField(default='', max_length=20, null=True),
        ),
    ]
