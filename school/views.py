import django
from django.shortcuts import render, get_object_or_404, redirect
from .models import DriverSchoolUnit, Alphabet, Area, DriverApplication, City, DriverSchool
from .forms import CreateApplicationForm, PartnershipForm


def home(request):
    schools, areas, letters, application, cities = DriverSchoolUnit.objects.all(), Area.objects.all(), Alphabet.objects.all(), DriverApplication.objects.all(), City.objects.all()
    dict_home = {'areas': areas, 'schools': schools, 'letters': letters,
                 'create_application_form': CreateApplicationForm(),
                 'partnership_form': PartnershipForm(), 'len_apps': len(application),
                 'len_schools': len(schools), 'len_cities': len(cities)}
    return render(request, 'school/home.html', dict_home)


class Search:
    schools, areas, letters, application, cities = DriverSchoolUnit.objects.all(), Area.objects.all(), Alphabet.objects.all(), DriverApplication.objects.all(), City.objects.all()
    ukraine_map = 'https://www.google.com/maps/embed?pb=!1m14!1m12!1m3!1d2375030.7670806646!2d31.679159930216635!3d49.268812139128045!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!5e0!3m2!1sru!2sua!4v1663054580432!5m2!1sru!2sua'

    @classmethod
    def django_dict_search(cls, info, searched, cities_of_unit=None, error=None):
        match error:
            case 'Not found, please input another word':
                return {'areas': cls.areas, 'info': info, 'count': len(info),
                        'create_application_form': CreateApplicationForm(),
                        'partnership_form': PartnershipForm(), 'searched': searched,
                        'error': error}

            case _:
                return {'areas': cls.areas, 'info': info, 'count': len(info),
                        'create_application_form': CreateApplicationForm(),
                        'partnership_form': PartnershipForm(), 'searched': searched,
                        'url_city': ''.join([cls.ukraine_map, info[0].city_of_unit.url][searched in cities_of_unit]),
                        'error': error}

    @classmethod
    def django_home_dict(cls, error=None):

        return {'areas': cls.areas, 'schools': cls.schools, 'letters': cls.letters,
                'create_application_form': CreateApplicationForm(),
                'partnership_form': PartnershipForm(), 'len_apps': len(cls.application),
                'len_schools': len(cls.schools), 'len_cities': len(cls.cities), 'error': error}

    @classmethod
    def search_city(cls, request, searched):

        django_search_city = DriverSchoolUnit.objects.filter(city_of_unit__name__contains=searched.capitalize())

        if django_search_city:
            cities_of_unit = [_.city_of_unit.name for _ in django_search_city]

            return render(request, 'school/search_schools.html',
                          cls.django_dict_search(django_search_city, searched, cities_of_unit))

        return render(request, 'school/search_schools.html',
                      cls.django_dict_search(django_search_city, searched,
                                             error='Not found, please input another word'))

    @classmethod
    def search_post_code(cls, request, searched):

        django_search_code = DriverSchoolUnit.objects.filter(city_of_unit__post_code__contains=searched)

        match searched[0]:
            case '0':
                post_code_of_unit = [_.city_of_unit.post_code for _ in django_search_code]

                return render(request, 'school/search_schools.html',
                              cls.django_dict_search(django_search_code, searched, post_code_of_unit))

            case _:
                return render(request, 'school/search_schools.html',
                              cls.django_dict_search(django_search_code, searched,
                                                     error='Not found, please input another word'))

    @classmethod
    def home_search(cls, request):
        if request.GET['searched']:
            searched = request.GET['searched']
            match searched[0]:
                case '0':
                    return cls.search_post_code(request, searched)

                case _:
                    return cls.search_city(request, searched)

        home_dict = cls.django_home_dict('Please input')
        return render(request, 'school/home.html', home_dict)

    @classmethod
    def main_search(cls, request, searched):
        match searched[0]:
            case '0':
                return cls.search_post_code(request, searched)

            case _:
                return cls.search_city(request, searched)


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
                '-' + filter_value_in_key[request.GET.get('filtered')])

            if ordered_schools:
                dict_filter_order_code = {'areas': areas, 'filtered_schools': ordered_schools,
                                          'count': len(ordered_schools),
                                          'url_city': ''.join([ukraine_map, ordered_schools[0].city_of_unit.url][
                                                                  city in filter_cities or city in filter_post_code]),
                                          'create_application_form': CreateApplicationForm(),
                                          'partnership_form': PartnershipForm(), 'searched': city}

                return render(request, 'school/filtered_schools.html',
                              dict_filter_order_code)
            else:
                dict_filter_order_code = {'areas': areas, 'filtered_schools': ordered_schools,
                                          'count': len(ordered_schools),
                                          'url_city': ukraine_map,

                                          'create_application_form': CreateApplicationForm(),
                                          'partnership_form': PartnershipForm(), 'searched': city,
                                          'error': 'Not found result'}

                return render(request, 'school/search_schools.html',
                              dict_filter_order_code)
        else:
            ordered_schools = filtered_schools.order_by(filter_value_in_key[request.GET.get('filtered')])
            if ordered_schools:

                dict_filter_order_code = {'areas': areas, 'filtered_schools': ordered_schools,
                                          'count': len(ordered_schools),
                                          'url_city': ''.join([ukraine_map, ordered_schools[0].city_of_unit.url][
                                                                  city in filter_cities or city in filter_post_code]),

                                          'create_application_form': CreateApplicationForm(),
                                          'partnership_form': PartnershipForm(), 'searched': city}

                return render(request, 'school/filtered_schools.html',
                              dict_filter_order_code)
            else:
                dict_filter_order_code = {'areas': areas, 'filtered_schools': ordered_schools,
                                          'count': len(ordered_schools),
                                          'url_city': ukraine_map,

                                          'create_application_form': CreateApplicationForm(),
                                          'partnership_form': PartnershipForm(), 'searched': city,
                                          'error': 'Not found result'}

                return render(request, 'school/search_schools.html',
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
        if category_filtered:
            dict_category_filter = {'areas': areas,
                                    'filtered_schools': category_filtered, 'count': len(category_filtered),
                                    'url_city': ''.join([ukraine_map, category_filtered[0].city_of_unit.url][
                                                            city in filter_cities or city in filter_post_code]),
                                    'create_application_form': CreateApplicationForm(),
                                    'partnership_form': PartnershipForm(), 'searched': city}

            return render(request, 'school/filtered_schools.html',
                          dict_category_filter)
        else:
            dict_filter_order_code = {'areas': areas, 'filtered_schools': category_filtered,
                                      'count': len(category_filtered),
                                      'url_city': ukraine_map,

                                      'create_application_form': CreateApplicationForm(),
                                      'partnership_form': PartnershipForm(), 'searched': city,
                                      'error': 'Not found result'}

            return render(request, 'school/search_schools.html',
                          dict_filter_order_code)


# Info about school
def info_about_authoschool(request, school_pk):
    areas, school_unit, app_form, partnership_form, school = Area.objects.all(), \
                                                             get_object_or_404(DriverSchoolUnit, pk=school_pk), \
                                                             CreateApplicationForm(), PartnershipForm(), \
                                                             get_object_or_404(DriverSchool, pk=school_pk)
    return render(request, 'school/school_info.html',
                  {'areas': areas, 'school_unit': school_unit, 'url_address': school_unit.url, 'school': school,
                   'create_application_form': app_form,
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
            schools, areas, letters, application, cities = DriverSchoolUnit.objects.all(), Area.objects.all(), Alphabet.objects.all(), DriverApplication.objects.all(), City.objects.all()
            dict_home = {'areas': areas, 'schools': schools, 'letters': letters,
                         'create_application_form': form,
                         'partnership_form': PartnershipForm(), 'len_apps': len(application),
                         'len_schools': len(schools), 'len_cities': len(cities)}
            return render(request, 'school/home.html', dict_home)
    else:
        schools, areas, letters, application, cities = DriverSchoolUnit.objects.all(), Area.objects.all(), Alphabet.objects.all(), DriverApplication.objects.all(), City.objects.all()
        dict_home = {'areas': areas, 'schools': schools, 'letters': letters,
                     'create_application_form': CreateApplicationForm(),
                     'partnership_form': PartnershipForm(), 'len_apps': len(application),
                     'len_schools': len(schools), 'len_cities': len(cities)}
        return render(request, 'school/home.html', dict_home)


def create_partnership_app(request):
    if request.method == 'POST':
        form = PartnershipForm(request.POST)
        if form.is_valid():
            new_app = form.save(commit=False)
            new_app.user = request.user
            new_app.save()
            return redirect('home')
        else:
            schools, areas, letters, application, cities = DriverSchoolUnit.objects.all(), Area.objects.all(), Alphabet.objects.all(), DriverApplication.objects.all(), City.objects.all()
            dict_home = {'areas': areas, 'schools': schools, 'letters': letters,
                         'create_application_form': CreateApplicationForm(),
                         'partnership_form': form, 'len_apps': len(application),
                         'len_schools': len(schools), 'len_cities': len(cities)}
            return render(request, 'school/home.html', dict_home)
    else:
        schools, areas, letters, application, cities = DriverSchoolUnit.objects.all(), Area.objects.all(), Alphabet.objects.all(), DriverApplication.objects.all(), City.objects.all()
        dict_home = {'areas': areas, 'schools': schools, 'letters': letters,
                     'create_application_form': CreateApplicationForm(),
                     'partnership_form': PartnershipForm(), 'len_apps': len(application),
                     'len_schools': len(schools), 'len_cities': len(cities)}
        return render(request, 'school/home.html', dict_home)
