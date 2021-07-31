# Generated by Django 3.2.4 on 2021-07-16 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounting', '0002_auto_20210714_1115'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accountingdata',
            old_name='Exceptiom_level',
            new_name='exceptiom_level',
        ),
        migrations.RenameField(
            model_name='accountingdata',
            old_name='Exception_BusinessLine',
            new_name='exception_BusinessLine',
        ),
        migrations.RenameField(
            model_name='accountingdata',
            old_name='Exception_COBDT',
            new_name='exception_COBDT',
        ),
        migrations.RenameField(
            model_name='accountingdata',
            old_name='Exception_ID',
            new_name='exception_ID',
        ),
        migrations.RenameField(
            model_name='accountingdata',
            old_name='Exception_LegalEntity',
            new_name='exception_LegalEntity',
        ),
        migrations.RenameField(
            model_name='accountingdata',
            old_name='Exception_ProfitCenter',
            new_name='exception_ProfitCenter',
        ),
        migrations.RenameField(
            model_name='accountingdata',
            old_name='Exception_Region',
            new_name='exception_Region',
        ),
        migrations.RenameField(
            model_name='accountingdata',
            old_name='Exception_description',
            new_name='exception_description',
        ),
        migrations.RenameField(
            model_name='accountingdata',
            old_name='Exception_name',
            new_name='exception_name',
        ),
        migrations.RemoveField(
            model_name='accountingdata',
            name='Exception_component',
        ),
        migrations.AddField(
            model_name='accountingdata',
            name='exception_component',
            field=models.CharField(default='', max_length=20, null=True),
        ),
    ]