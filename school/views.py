from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Count
from .models import DriverSchoolUnit, Alphabet, Area, DriverApplication, City
from .forms import CreateApplicationForm, PartnershipForm


def home(request):
    schools, areas, letters, application, cities = DriverSchoolUnit.objects.all(), Area.objects.all(), Alphabet.objects.all(), \
                                                   DriverApplication.objects.all(), City.objects.all()
    dict_home = {'areas': areas, 'schools': schools, 'letters': letters,
                 'create_application_form': CreateApplicationForm(),
                 'partnership_form': PartnershipForm(), 'len_apps': len(application),
                 'len_schools': len(schools), 'len_cities': len(cities)}
    return render(request, 'school/home.html', dict_home)


# Search schools code_city/city
def search_authoschool(request, searched):
    areas = Area.objects.all()

    django_search_school_city = DriverSchoolUnit.objects.filter(city_of_unit__name__contains=searched.capitalize())
    django_search_school_code = DriverSchoolUnit.objects.filter(city_of_unit__post_code__contains=searched)

    if django_search_school_city:
        city_autoschools = django_search_school_city

        dict_search_school_city = {'areas': areas, 'info': city_autoschools, 'count': len(city_autoschools),
                                   'name_city': city_autoschools[0].city_of_unit,
                                   'url_city': city_autoschools[0].city_of_unit.url,
                                   'create_application_form': CreateApplicationForm(),
                                   'partnership_form': PartnershipForm(), }

        return render(request, 'school/search_schools.html',
                      dict_search_school_city)

    if django_search_school_code:

        city_autoschools = django_search_school_code

        dict_search_school_code = {'areas': areas, 'info': city_autoschools, 'count': len(city_autoschools),
                                   'name_city': city_autoschools[0].city_of_unit,
                                   'url_city': city_autoschools[0].city_of_unit.url,
                                   'create_application_form': CreateApplicationForm(),
                                   'partnership_form': PartnershipForm(), }

        return render(request, 'school/search_schools.html', dict_search_school_code)

    else:
        return render(request, 'school/error404.html')


def search(request):
    if request.GET['searched']:
        areas, searched = Area.objects.all(), request.GET['searched']

        django_search_city = DriverSchoolUnit.objects.filter(city_of_unit__name__contains=searched.capitalize())
        django_search_code = DriverSchoolUnit.objects.filter(city_of_unit__post_code__contains=searched)

        if django_search_city:
            city_autoschools = django_search_city

            dict_search_city = {'areas': areas, 'info': city_autoschools, 'count': len(city_autoschools),
                                'name_city': city_autoschools[0].city_of_unit,
                                'url_city': city_autoschools[0].city_of_unit.url,
                                'create_application_form': CreateApplicationForm(),
                                'partnership_form': PartnershipForm(), }

            return render(request, 'school/search_schools.html',
                          dict_search_city)
        if django_search_code:

            city_autoschools = django_search_code

            dict_search_code = {'areas': areas, 'info': city_autoschools, 'count': len(city_autoschools),
                                'name_city': city_autoschools[0].city_of_unit,
                                'url_city': city_autoschools[0].city_of_unit.url,
                                'create_application_form': CreateApplicationForm(),
                                'partnership_form': PartnershipForm(), }

            return render(request, 'school/search_schools.html',
                          dict_search_code)
        else:
            return render(request, 'school/search_schools.html',
                          {'areas': areas, 'error': 'Not found, please input another word', 'name_city': 'Error'})
    else:

        schools, areas, letters = DriverSchoolUnit.objects.all(), Area.objects.all(), Alphabet.objects.all()

        dict_search_error = {'areas': areas, 'schools': schools, 'letters': letters,
                             'error': 'Please input',
                             'create_application_form': CreateApplicationForm(),
                             'partnership_form': PartnershipForm(), }

        return render(request, 'school/home.html', dict_search_error)


# for big filter
def filtered(request, city):
    areas, schools, letter = Area.objects.all(), DriverSchoolUnit.objects.all(), request.GET.get('category')

    filter_value_in_key = {
        "price-low-up": 'cources__price',
        "price-up-low": 'cources__price',
        'alphabet': 'driverschool__name',
        'rating': 'driverschool__score',
    }

    if city[0] == '0':
        if request.GET.get('filtered'):

            filtered_schools = DriverSchoolUnit.objects.filter(
                cources__category__name__contains=letter).filter(
                city_of_unit__post_code__contains=city)

            if request.GET.get('filtered') == 'price-up-low' or request.GET.get('filtered') == 'rating':

                ordered_schools = filtered_schools.order_by(
                    '-' + filter_value_in_key[request.GET.get('filtered')]).distinct(
                    filter_value_in_key[request.GET.get('filtered')])

                dict_filter_order_code = {'areas': areas, 'filtered_schools': ordered_schools,
                                          'count': len(ordered_schools),
                                          'url_city': ordered_schools[0].city_of_unit.url,
                                          'name_city': ordered_schools[0].city_of_unit,
                                          'create_application_form': CreateApplicationForm(),
                                          'partnership_form': PartnershipForm(), }

                return render(request, 'school/filtered_schools.html',
                              dict_filter_order_code)
            else:
                ordered_schools = filtered_schools.order_by(filter_value_in_key[request.GET.get('filtered')]).distinct(
                    filter_value_in_key[request.GET.get('filtered')])

                dict_filter_order_code = {'areas': areas, 'filtered_schools': ordered_schools,
                                          'count': len(ordered_schools),
                                          'url_city': ordered_schools[0].city_of_unit.url,
                                          'name_city': ordered_schools[0].city_of_unit,
                                          'create_application_form': CreateApplicationForm(),
                                          'partnership_form': PartnershipForm(), }

                return render(request, 'school/filtered_schools.html',
                              dict_filter_order_code)
        else:

            category_filtered = DriverSchoolUnit.objects.filter(
                cources__category__name__contains=letter).filter(
                city_of_unit__post_code__contains=city)

            dict_category_filter = {'areas': areas,
                                    'filtered_schools': category_filtered, 'count': len(category_filtered),
                                    'url_city': category_filtered[0].city_of_unit.url,
                                    'name_city': category_filtered[0].city_of_unit,
                                    'create_application_form': CreateApplicationForm(),
                                    'partnership_form': PartnershipForm(), }
            return render(request, 'school/filtered_schools.html',
                          dict_category_filter)

    else:
        if request.GET.get('filtered'):

            filtered_schools = DriverSchoolUnit.objects.filter(
                cources__category__name__contains=letter).filter(
                city_of_unit__name__contains=city)

            if request.GET.get('filtered') == 'price-up-low' or request.GET.get('filtered') == 'rating':

                ordered_schools = filtered_schools.order_by(
                    '-' + filter_value_in_key[request.GET.get('filtered')]).distinct(
                    filter_value_in_key[request.GET.get('filtered')])

                dict_filter_order_city = {'areas': areas, 'filtered_schools': ordered_schools,
                                          'count': len(ordered_schools),
                                          'url_city': ordered_schools[0].city_of_unit.url,
                                          'name_city': ordered_schools[0].city_of_unit,
                                          'create_application_form': CreateApplicationForm(),
                                          'partnership_form': PartnershipForm(), }

                return render(request, 'school/filtered_schools.html',
                              dict_filter_order_city)
            else:

                ordered_schools = filtered_schools.order_by(filter_value_in_key[request.GET.get('filtered')]).distinct(
                    filter_value_in_key[request.GET.get('filtered')])

                dict_filter_order_city = {'areas': areas, 'filtered_schools': ordered_schools,
                                          'count': len(ordered_schools),
                                          'url_city': ordered_schools[0].city_of_unit.url,
                                          'name_city': ordered_schools[0].city_of_unit,
                                          'create_application_form': CreateApplicationForm(),
                                          'partnership_form': PartnershipForm(), }

                return render(request, 'school/filtered_schools.html',
                              dict_filter_order_city)
        else:

            category_filtered = DriverSchoolUnit.objects.filter(
                cources__category__name__contains=letter).filter(
                city_of_unit__name__contains=city)

            dict_category_filter = {'areas': areas,
                                    'filtered_schools': category_filtered, 'count': len(category_filtered),
                                    'url_city': category_filtered[0].city_of_unit.url,
                                    'name_city': category_filtered[0].city_of_unit,
                                    'create_application_form': CreateApplicationForm(),
                                    'partnership_form': PartnershipForm(), }

            return render(request, 'school/filtered_schools.html',
                          dict_category_filter)


# Info about school
def info_about_authoschool(request, school_pk):
    areas, school, app_form, partnership_form = Area.objects.all(), get_object_or_404(DriverSchoolUnit,
                                                                                      pk=school_pk), \
                                                CreateApplicationForm(), PartnershipForm()
    return render(request, 'school/school_info.html',
                  {'areas': areas, 'school': school, 'url_address': school.url, 'app_form': app_form,
                   'partnership_form': partnership_form})


# just html page
def base(request):
    schools, areas = DriverSchoolUnit.objects.all(), Area.objects.all()
    return render(request, 'school/base.html', {'areas': areas, 'schools': schools})


# just html page
def footer(request):
    areas = Area.objects.all()
    create_application_form, partnership_form = CreateApplicationForm(), PartnershipForm()
    return render(request, 'school/footer.html', {'areas': areas, 'create_application_form': CreateApplicationForm(),
                                                  'partnership_form': partnership_form})


# just html page
def error404(request):
    schools, areas, create_application_form, partnership_form = DriverSchoolUnit.objects.all(), Area.objects.all(), \
                                                                CreateApplicationForm(), PartnershipForm()
    return render(request, 'school/error404.html',
                  {'areas': areas, 'schools': schools, 'create_application_form': create_application_form,
                   'partnership_form': partnership_form})


def create_driver_application(request):
    if request.method == 'POST':
        form = CreateApplicationForm(request.POST)
        if form.is_valid():
            new_app = form.save(commit=False)
            new_app.user = request.user
            new_app.save()
            return redirect('home')
        else:
            return render(request, 'school/error404.html',
                          {'create_application_form': form,
                           'partnership_form': PartnershipForm()})

    else:
        schools, areas = DriverSchoolUnit.objects.all(), Area.objects.all()
        return render(request, 'school/error404.html',
                      {'areas': areas, 'schools': schools, 'create_application_form': CreateApplicationForm(),
                       'partnership_form': PartnershipForm()})


def create_partnership_app(request):
    if request.method == 'POST':
        form = PartnershipForm(request.POST)
        if form.is_valid():
            new_app = form.save(commit=False)
            new_app.user = request.user
            new_app.save()
            return redirect('home')
        else:
            return render(request, 'school/error404.html',
                          {'create_application_form': CreateApplicationForm(),
                           'partnership_form': form})
    else:
        schools, areas = DriverSchoolUnit.objects.all(), Area.objects.all()
        return render(request, 'school/error404.html',
                      {'areas': areas, 'schools': schools, 'create_application_form': CreateApplicationForm(),
                       'partnership_form': PartnershipForm()})
