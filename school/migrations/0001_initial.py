# Generated by Django 4.1.1 on 2022-11-10 20:19

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomeDriverApp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstLast_name', models.CharField(max_length=50, verbose_name='ПІБ')),
                ('phone_number', models.CharField(max_length=20, verbose_name='Контактний номер тел.')),
                ('email', models.CharField(max_length=100, verbose_name='Контактний email')),
                ('status', models.IntegerField(default=0, verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Головна Заявка',
                'verbose_name_plural': 'Головна Заявки',
                'ordering': ['firstLast_name'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SchoolDriverApp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstLast_name', models.CharField(max_length=50, verbose_name='ПІБ')),
                ('phone_number', models.CharField(max_length=20, verbose_name='Контактний номер тел.')),
                ('email', models.CharField(max_length=100, verbose_name='Контактний email')),
                ('status', models.IntegerField(default=0, verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Автошкола Заявка',
                'verbose_name_plural': 'Автошкола Заявки',
                'ordering': ['firstLast_name'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Alphabet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('letter', models.CharField(max_length=3, verbose_name='Літера')),
                ('city_of_alphabet', models.CharField(max_length=1000, verbose_name='Міста за буквою')),
            ],
            options={
                'verbose_name': 'Алфавіт-Місто',
                'verbose_name_plural': 'Алфавіт-Місто',
                'ordering': ['letter'],
            },
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Назва області')),
                ('cities', models.CharField(blank=True, max_length=1000, verbose_name='Міста області')),
            ],
            options={
                'verbose_name': 'Область',
                'verbose_name_plural': 'Області',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Назва категорії')),
                ('description', models.CharField(max_length=128, verbose_name='Опис')),
            ],
            options={
                'verbose_name': 'Категорія водіння',
                'verbose_name_plural': 'Категорії водіння',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Назва міста')),
                ('post_code', models.CharField(max_length=16, verbose_name='Поштовий індекс')),
                ('url', models.URLField(blank=True, max_length=400, verbose_name='Геопозиція міста')),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.area', verbose_name='Область')),
            ],
            options={
                'verbose_name': 'Місто',
                'verbose_name_plural': 'Міста',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_description', models.CharField(max_length=64, verbose_name='Опис')),
                ('price', models.IntegerField(default=0, verbose_name='Вартість')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.category', verbose_name='Категорія')),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курси',
                'ordering': ['short_description'],
            },
        ),
        migrations.CreateModel(
            name='DriverSchool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=46, verbose_name='Назва автошколи')),
                ('address', models.CharField(max_length=60, verbose_name='Адреса головного офісу')),
                ('unit', models.BooleanField(default=False, verbose_name='Наявність філій')),
                ('contact', models.CharField(max_length=28, verbose_name='Контактний номер тел.')),
                ('email', models.CharField(blank=True, max_length=30, verbose_name='Контактний email')),
                ('description', models.TextField(blank=True, verbose_name='Опис')),
                ('image1', models.ImageField(default='school/images/test-image.jpg', upload_to='school/images/', verbose_name='Фото головне')),
                ('image2', models.ImageField(default='school/images/test-image.jpg', upload_to='school/images/', verbose_name='Фото 2')),
                ('image3', models.ImageField(default='school/images/test-image.jpg', upload_to='school/images/', verbose_name='Фото 3')),
                ('image4', models.ImageField(default='school/images/test-image.jpg', upload_to='school/images/', verbose_name='Фото 4')),
                ('image5', models.ImageField(default='school/images/test-image.jpg', upload_to='school/images/', verbose_name='Фото 5')),
                ('score', models.IntegerField(validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)], verbose_name='Рейтинг')),
                ('area', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='school.area', verbose_name='Область')),
                ('city', smart_selects.db_fields.ChainedForeignKey(chained_field='area', chained_model_field='area', on_delete=django.db.models.deletion.CASCADE, to='school.city', verbose_name='Місто')),
            ],
            options={
                'verbose_name': 'Автошкола',
                'verbose_name_plural': 'Автошколи',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Partnership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstLast_name', models.CharField(max_length=50, verbose_name='ПІБ')),
                ('phone_number', models.CharField(max_length=20, verbose_name='Контактний номер тел.')),
                ('email', models.CharField(max_length=100, verbose_name='Контактний email')),
                ('description', models.TextField(blank=True, verbose_name='Опис')),
            ],
            options={
                'verbose_name': 'Партнер',
                'verbose_name_plural': 'Партнери',
                'ordering': ['firstLast_name'],
            },
        ),
        migrations.CreateModel(
            name='DriverSchoolUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=46, verbose_name='Назва філії')),
                ('address', models.CharField(max_length=60, verbose_name='Адреса автошколи')),
                ('url', models.URLField(blank=True, max_length=1500, verbose_name='Геопозиція автошколи')),
                ('contact', models.CharField(max_length=28, verbose_name='Контактний номер тел.')),
                ('area', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='school.area', verbose_name='Область')),
                ('category', models.ManyToManyField(blank=True, to='school.category', verbose_name='Категорії')),
                ('city_of_unit', smart_selects.db_fields.ChainedForeignKey(chained_field='area', chained_model_field='area', on_delete=django.db.models.deletion.CASCADE, to='school.city', verbose_name='Місто')),
                ('cources', smart_selects.db_fields.ChainedManyToManyField(blank='True', chained_field='category', chained_model_field='category', to='school.courses', verbose_name='Курси')),
                ('driverschool', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.driverschool', verbose_name='Головний офіс')),
            ],
            options={
                'verbose_name': 'Філія автошколи',
                'verbose_name_plural': 'Філії автошкіл',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='DriverApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstLast_name', models.CharField(max_length=50, verbose_name='ПІБ')),
                ('phone_number', models.CharField(max_length=20, verbose_name='Контактний номер тел.')),
                ('email', models.CharField(max_length=100, verbose_name='Контактний email')),
                ('status', models.IntegerField(default=0, verbose_name='Статус')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.city', verbose_name='Місто')),
                ('course', smart_selects.db_fields.ChainedForeignKey(chained_field='driverschoolunit', chained_model_field='driverschoolunit', on_delete=django.db.models.deletion.CASCADE, to='school.courses', verbose_name='Курс')),
                ('driverschoolunit', smart_selects.db_fields.ChainedForeignKey(chained_field='city', chained_model_field='city_of_unit', on_delete=django.db.models.deletion.CASCADE, to='school.driverschoolunit', verbose_name='Філія автошколи')),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявки',
                'ordering': ['firstLast_name'],
            },
        ),
    ]
