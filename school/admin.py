from django.contrib import admin
from .models import Area, City, Category, Courses, DriverSchool, DriverSchoolUnit, Partnership, DriverApplication, \
    Alphabet
from django import forms
from import_export.admin import ImportExportModelAdmin


@admin.register(Area)
class AreaAdmin(ImportExportModelAdmin):
    fields = ('name', 'cities')


class CityAdminForm(forms.ModelForm):
    class Meta:
        model = City
        fields = '__all__'


class CityAdmin(admin.ModelAdmin):
    form = CityAdminForm
    list_display = ('name', 'post_code',)
    list_display_links = ('name', 'post_code')
    search_fields = ('name',)
    list_filter = ('area',)


class CategoryAdminForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class CategoryAdmin(admin.ModelAdmin):
    form = CategoryAdminForm
    fields = ('name', 'description')
    list_display = ('name', 'description',)


class CoursesAdminForm(forms.ModelForm):
    class Meta:
        model = Courses
        fields = '__all__'


class CoursesAdmin(admin.ModelAdmin):
    form = CoursesAdminForm
    list_display = ('short_description', 'price',)
    list_display_links = ('short_description', 'price')
    search_fields = ('short_description',)
    list_filter = ('category',)


class DriverSchoolAdminForm(forms.ModelForm):
    class Meta:
        model = DriverSchool
        fields = '__all__'


class DriverSchoolAdmin(admin.ModelAdmin):
    form = DriverSchoolAdminForm
    list_display = ('name', 'address',)
    list_display_links = ('name', 'address')
    search_fields = ('name', 'address',)
    list_filter = ('city',)
    fields = (
        'name', 'address', 'unit', 'contact', 'email', 'city', 'description', 'image1', 'image2', 'image3',
        'image4',
        'image5', 'score')


class DriverSchoolUnitAdminForm(forms.ModelForm):
    class Meta:
        model = DriverSchoolUnit
        fields = '__all__'


class DriverSchoolUnitAdmin(admin.ModelAdmin):
    form = DriverSchoolUnitAdminForm
    list_display = ('name', 'address',)
    list_display_links = ('name', 'address')
    search_fields = ('name', 'address',)
    list_filter = ('city_of_unit',)
    fields = ('name', 'address', 'driverschool', 'url', 'category', 'cources', 'contact', 'city_of_unit')


class PartnershipAdminForm(forms.ModelForm):
    class Meta:
        model = Partnership
        fields = '__all__'


class PartnershipAdmin(admin.ModelAdmin):
    form = PartnershipAdminForm
    list_display = ('first_name', 'last_name',)
    list_display_links = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name',)
    fields = ('first_name', 'last_name', 'phone_number', 'email', 'description')


class DriverApplicationAdminForm(forms.ModelForm):
    class Meta:
        model = DriverApplication
        fields = '__all__'


class DriverApplicationAdmin(admin.ModelAdmin):
    form = DriverApplicationAdminForm
    list_display = ('first_name', 'last_name',)
    list_display_links = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name',)
    list_filter = ('driverschoolunit',)
    fields = ('first_name', 'last_name', 'phone_number', 'email', 'driverschoolunit', 'сourse')


@admin.register(Alphabet)
class AlphabetAdmin(ImportExportModelAdmin):
    fields = ('letter', 'city_of_alphabet')


admin.site.site_title = "Адміністрування"
admin.site.site_header = "Адміністрування"

admin.site.register(City, CityAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Courses, CoursesAdmin)
admin.site.register(DriverSchool, DriverSchoolAdmin)
admin.site.register(DriverSchoolUnit, DriverSchoolUnitAdmin)
admin.site.register(Partnership, PartnershipAdmin)
admin.site.register(DriverApplication, DriverApplicationAdmin)

# Register your models here.
