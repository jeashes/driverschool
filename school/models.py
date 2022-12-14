from django.db import models
from django import core
from django.urls import reverse
from smart_selects.db_fields import ChainedManyToManyField, ChainedForeignKey


class Area(models.Model):
    name = models.CharField(max_length=50, verbose_name='Назва області')
    slug = models.SlugField(max_length=50, verbose_name='URL', unique=True)
    cities = models.CharField(max_length=1000, verbose_name='Міста області', blank=True)
    objects = models.Manager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('area', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Область'
        verbose_name_plural = 'Області'
        ordering = ['name']


class City(models.Model):
    name = models.CharField(max_length=50, verbose_name='Назва міста')
    slug = models.SlugField(max_length=50, verbose_name='URL', unique=True)
    post_code = models.CharField(max_length=16, verbose_name='Поштовий індекс')
    area = models.ForeignKey(Area, on_delete=models.CASCADE, verbose_name='Область')
    url = models.URLField(max_length=400, blank=True, verbose_name='Геопозиція міста')
    objects = models.Manager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('city', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Місто'
        verbose_name_plural = 'Міста'
        ordering = ['name']


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Назва категорії')
    description = models.CharField(max_length=128, verbose_name='Опис')
    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категорія водіння'
        verbose_name_plural = 'Категорії водіння'
        ordering = ['name']


class Courses(models.Model):
    short_description = models.CharField(max_length=64, verbose_name='Опис')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категорія')
    price = models.IntegerField(default=0, verbose_name='Вартість')
    objects = models.Manager()

    def __str__(self):
        return self.short_description

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курси'
        ordering = ['short_description']


class DriverSchool(models.Model):
    name = models.CharField(max_length=46, verbose_name='Назва автошколи')
    address = models.CharField(max_length=60, verbose_name='Адреса головного офісу')
    unit = models.BooleanField(verbose_name='Наявність філій', default=False)
    contact = models.CharField(max_length=28, verbose_name='Контактний номер тел.')
    email = models.CharField(max_length=30, verbose_name='Контактний email', blank=True)
    area = models.ForeignKey(Area, on_delete=models.CASCADE, blank=True, verbose_name='Область')
    city = ChainedForeignKey(City, chained_field='area', chained_model_field='area', on_delete=models.CASCADE,
                             verbose_name='Місто')
    description = models.TextField(blank=True, verbose_name='Опис')
    image1 = models.ImageField(upload_to='school/images/', default='school/images/test-image.jpg',
                               verbose_name='Фото головне')
    image2 = models.ImageField(upload_to='school/images/', default='school/images/test-image.jpg',
                               verbose_name='Фото 2')
    image3 = models.ImageField(upload_to='school/images/', default='school/images/test-image.jpg',
                               verbose_name='Фото 3')
    image4 = models.ImageField(upload_to='school/images/', default='school/images/test-image.jpg',
                               verbose_name='Фото 4')
    image5 = models.ImageField(upload_to='school/images/', default='school/images/test-image.jpg',
                               verbose_name='Фото 5')
    score = models.IntegerField(validators=[
        core.validators.MaxValueValidator(5),
        core.validators.MinValueValidator(0),
    ], verbose_name='Рейтинг'
    )
    objects = models.Manager()

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = 'Автошкола'
        verbose_name_plural = 'Автошколи'
        ordering = ['name']


class DriverSchoolUnit(models.Model):
    name = models.CharField(max_length=46, verbose_name='Назва філії')
    address = models.CharField(max_length=60, verbose_name='Адреса автошколи')
    slug = models.SlugField(max_length=50, verbose_name='URL', unique=True)

    driverschool = models.ForeignKey(DriverSchool, on_delete=models.CASCADE, verbose_name='Головний офіс')
    url = models.URLField(max_length=1500, blank=True, verbose_name='Геопозиція автошколи')
    category = models.ManyToManyField(Category, verbose_name='Категорії', blank=True)
    cources = ChainedManyToManyField(Courses, chained_field='category', chained_model_field='category',
                                     verbose_name='Курси', blank='True')
    contact = models.CharField(max_length=28, verbose_name='Контактний номер тел.')
    area = models.ForeignKey(Area, on_delete=models.CASCADE, blank=True, verbose_name='Область')
    city_of_unit = ChainedForeignKey(City, chained_field='area', chained_model_field='area', on_delete=models.CASCADE,
                                     verbose_name='Місто')
    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Філія автошколи'
        verbose_name_plural = 'Філії автошкіл'
        ordering = ['name']


class Partnership(models.Model):
    firstLast_name = models.CharField(max_length=50, verbose_name='ПІБ')
    phone_number = models.CharField(max_length=20, verbose_name='Контактний номер тел.')
    email = models.CharField(max_length=100, verbose_name='Контактний email')
    description = models.TextField(blank=True, verbose_name='Опис')
    objects = models.Manager()

    def __str__(self):
        return self.firstLast_name

    class Meta:
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнери'
        ordering = ['firstLast_name']


class DriverApplication(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='Місто')
    driverschoolunit = ChainedForeignKey(DriverSchoolUnit, chained_field='city', chained_model_field="city_of_unit",
                                         on_delete=models.CASCADE, verbose_name='Філія автошколи')
    firstLast_name = models.CharField(max_length=50, verbose_name='ПІБ')
    phone_number = models.CharField(max_length=20, verbose_name='Контактний номер тел.')
    email = models.CharField(max_length=100, verbose_name='Контактний email')
    status = models.IntegerField(default=0, verbose_name='Статус')
    course = ChainedForeignKey(Courses, chained_field='driverschoolunit', chained_model_field="driverschoolunit",
                               on_delete=models.CASCADE, verbose_name='Курс')
    objects = models.Manager()

    def __str__(self):
        return self.firstLast_name

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        ordering = ['firstLast_name']


class Alphabet(models.Model):
    letter = models.CharField(max_length=3, verbose_name='Літера')
    slug = models.SlugField(max_length=50, verbose_name='URL', unique=True)
    city_of_alphabet = models.CharField(max_length=1000, verbose_name='Міста за буквою')
    objects = models.Manager()

    def __str__(self):
        return self.letter

    def get_absolute_url(self):
        return reverse('area', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Алфавіт-Місто'
        verbose_name_plural = 'Алфавіт-Місто'
        ordering = ['letter']


class SchoolDriverApp(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='Місто')
    driverschoolunit = models.ForeignKey(DriverSchoolUnit,
                                         on_delete=models.CASCADE, verbose_name='Філія автошколи')
    firstLast_name = models.CharField(max_length=50, verbose_name='ПІБ')
    phone_number = models.CharField(max_length=20, verbose_name='Контактний номер тел.')
    email = models.CharField(max_length=100, verbose_name='Контактний email')
    status = models.IntegerField(default=0, verbose_name='Статус')
    course = models.ForeignKey(Courses,
                               on_delete=models.CASCADE, verbose_name='Курс')
    objects = models.Manager()

    def __str__(self):
        return self.firstLast_name

    class Meta:
        managed = True
        verbose_name = 'Автошкола Заявка'
        verbose_name_plural = 'Автошкола Заявки'
        ordering = ['firstLast_name']


