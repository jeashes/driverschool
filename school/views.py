from django.shortcuts import render, get_object_or_404, redirect
from .models import DriverSchoolUnit, Alphabet, Area, DriverApplication, City
from .forms import CreateApplicationForm, PartnershipForm


def home(request):
    schools, areas, letters, application, cities = DriverSchoolUnit.objects.all(), Area.objects.all(), Alphabet.objects.all(), DriverApplication.objects.all(), City.objects.all()
    dict_home = {'areas': areas, 'schools': schools, 'letters': letters,
                 'create_application_form': CreateApplicationForm(),
                 'partnership_form': PartnershipForm(), 'len_apps': len(application),
                 'len_schools': len(schools), 'len_cities': len(cities)}
    return render(request, 'school/home.html', dict_home)


# Search schools code_city/city
def search_authoschool(request, searched):
    areas = Area.objects.all()

    django_search_city = DriverSchoolUnit.objects.filter(city_of_unit__name__contains=searched.capitalize())
    django_search_code = DriverSchoolUnit.objects.filter(city_of_unit__post_code__contains=searched)

    ukraine_map = 'https://www.google.com/maps/embed?pb=!1m14!1m12!1m3!1d2375030.7670806646!2d31.679159930216635!3d49.268812139128045!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!5e0!3m2!1sru!2sua!4v1663054580432!5m2!1sru!2sua'

    if django_search_city:
        city_autoschools = django_search_city

        cities_of_unit = [_.city_of_unit.name for _ in city_autoschools]

        dict_search_city = {'areas': areas, 'info': city_autoschools, 'count': len(city_autoschools),
                            'create_application_form': CreateApplicationForm(),
                            'partnership_form': PartnershipForm(), 'searched': searched,
                            'url_city': ''.join([ukraine_map, city_autoschools[0].city_of_unit.url][
                                                    searched in cities_of_unit])}

        return render(request, 'school/search_schools.html',
                      dict_search_city)

    if django_search_code:

        city_autoschools = django_search_code

        post_code_of_unit = [_.city_of_unit.post_code for _ in city_autoschools]

        dict_search_code = {'areas': areas, 'info': city_autoschools, 'count': len(city_autoschools),
                            'url_city': ''.join([ukraine_map, city_autoschools[0].city_of_unit.url][
                                                    searched in post_code_of_unit]),
                            'create_application_form': CreateApplicationForm(),
                            'partnership_form': PartnershipForm(), 'searched': searched}

        return render(request, 'school/search_schools.html',
                      dict_search_code)

    else:
        return render(request, 'school/error404.html')


def search(request):
    if request.GET['searched']:
        areas, searched = Area.objects.all(), request.GET['searched']

        django_search_city = DriverSchoolUnit.objects.filter(city_of_unit__name__contains=searched.capitalize())
        django_search_code = DriverSchoolUnit.objects.filter(city_of_unit__post_code__contains=searched)

        ukraine_map = 'https://www.google.com/maps/embed?pb=!1m14!1m12!1m3!1d2375030.7670806646!2d31.679159930216635!3d49.268812139128045!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!5e0!3m2!1sru!2sua!4v1663054580432!5m2!1sru!2sua'

        if django_search_city:
            city_autoschools = django_search_city

            cities_of_unit = [city.city_of_unit.name for city in city_autoschools]

            dict_search_city = {'areas': areas, 'info': city_autoschools, 'count': len(city_autoschools),
                                'create_application_form': CreateApplicationForm(),
                                'partnership_form': PartnershipForm(), 'searched': searched,
                                'url_city': ''.join([ukraine_map, city_autoschools[0].city_of_unit.url][
                                                        searched in cities_of_unit])}

            return render(request, 'school/search_schools.html',
                          dict_search_city)

        if django_search_code:

            city_autoschools = django_search_code

            post_code_of_unit = [city.city_of_unit.post_code for city in city_autoschools]

            dict_search_code = {'areas': areas, 'info': city_autoschools, 'count': len(city_autoschools),
                                'url_city': ''.join([ukraine_map, city_autoschools[0].city_of_unit.url][
                                                        searched in post_code_of_unit]),
                                'create_application_form': CreateApplicationForm(),
                                'partnership_form': PartnershipForm(), 'searched': searched}

            return render(request, 'school/search_schools.html',
                          dict_search_code)
        else:
            return render(request, 'school/search_schools.html',
                          {'areas': areas, 'error': 'Not found, please input another word', 'searched': 'Error'})
    else:

        schools, areas, letters, application, cities = DriverSchoolUnit.objects.all(), Area.objects.all(), Alphabet.objects.all(), DriverApplication.objects.all(), City.objects.all()

        dict_search_error = {'areas': areas, 'schools': schools, 'letters': letters,
                             'error': 'Please input',
                             'create_application_form': CreateApplicationForm(),
                             'partnership_form': PartnershipForm(), 'len_apps': len(application),
                             'len_schools': len(schools), 'len_cities': len(cities)}

        return render(request, 'school/home.html', dict_search_error)


# for big filter
def filtered(request, city):
    areas, schools, letter = Area.objects.all(), DriverSchoolUnit.objects.all(), request.GET.get('category')
    ukraine_map = 'https://www.google.com/maps/embed?pb=!1m14!1m12!1m3!1d2375030.7670806646!2d31.679159930216635!3d49.268812139128045!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!5e0!3m2!1sru!2sua!4v1663054580432!5m2!1sru!2sua'
    filter_value_in_key = {
        "price-low-up": 'cources__price',
        "price-up-low": 'cources__price',
        'alphabet': 'driverschool__name',
        'rating': 'driverschool__score',
    }

    if request.GET.get('filtered'):
        if city[0] == '0':
            filtered_schools = DriverSchoolUnit.objects.filter(
                cources__category__name__contains=letter).filter(
                city_of_unit__post_code__contains=city)
        else:
            filtered_schools = DriverSchoolUnit.objects.filter(
                cources__category__name__contains=letter).filter(
                city_of_unit__name__contains=city)

        filter_cities = [_.city_of_unit.name for _ in filtered_schools]
        filter_post_code = [_.city_of_unit.post_code for _ in filtered_schools]

        if request.GET.get('filtered') == 'price-up-low' or request.GET.get('filtered') == 'rating':

            ordered_schools = filtered_schools.order_by(
                '-' + filter_value_in_key[request.GET.get('filtered')]).distinct(
                filter_value_in_key[request.GET.get('filtered')])

            dict_filter_order_code = {'areas': areas, 'filtered_schools': ordered_schools,
                                      'count': len(ordered_schools),
                                      'url_city': ''.join([ukraine_map, ordered_schools[0].city_of_unit.url][
                                                              city in filter_cities or city in filter_post_code]),
                                      'create_application_form': CreateApplicationForm(),
                                      'partnership_form': PartnershipForm(), 'searched': city}

            return render(request, 'school/filtered_schools.html',
                          dict_filter_order_code)
        else:
            ordered_schools = filtered_schools.order_by(filter_value_in_key[request.GET.get('filtered')]).distinct(
                filter_value_in_key[request.GET.get('filtered')])

            dict_filter_order_code = {'areas': areas, 'filtered_schools': ordered_schools,
                                      'count': len(ordered_schools),
                                      'url_city': ''.join([ukraine_map, ordered_schools[0].city_of_unit.url][
                                                              city in filter_cities or city in filter_post_code]),

                                      'create_application_form': CreateApplicationForm(),
                                      'partnership_form': PartnershipForm(), 'searched': city}

            return render(request, 'school/filtered_schools.html',
                          dict_filter_order_code)
    else:

        if city[0] == '0':
            category_filtered = DriverSchoolUnit.objects.filter(
                cources__category__name__contains=letter).filter(
                city_of_unit__post_code__contains=city)
        else:
            category_filtered = DriverSchoolUnit.objects.filter(
                cources__category__name__contains=letter).filter(
                city_of_unit__name__contains=city)

        filter_cities = [_.city_of_unit.name for _ in category_filtered]

        filter_post_code = [_.city_of_unit.post_code for _ in category_filtered]

        dict_category_filter = {'areas': areas,
                                'filtered_schools': category_filtered, 'count': len(category_filtered),
                                'url_city': ''.join([ukraine_map, category_filtered[0].city_of_unit.url][
                                                        city in filter_cities or city in filter_post_code]),
                                'create_application_form': CreateApplicationForm(),
                                'partnership_form': PartnershipForm(), 'searched': city}
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
