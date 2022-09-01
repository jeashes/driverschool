# Generated by Django 4.1 on 2022-09-01 06:22

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_alter_driverapplication_course_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driverapplication',
            name='driverschoolunit',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='city', chained_model_field='city_of_unit', on_delete=django.db.models.deletion.CASCADE, to='school.driverschoolunit', verbose_name='Філія автошколи'),
        ),
    ]
