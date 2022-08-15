from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from .models import DriverSchoolUnit, Alphabet, Area


def home(request):
    schools, areas, letters = DriverSchoolUnit.objects.all(), Area.objects.all(), Alphabet.objects.all()
    return render(request, 'school/home.html', {'areas': areas, 'schools': schools, 'letters': letters})


# Search schools code_city/city
def search_authoschool(request, searched):
    areas = Area.objects.all()
    if DriverSchoolUnit.objects.filter(city_of_unit__name__contains=searched):
        city_authoschools = DriverSchoolUnit.objects.filter(city_of_unit__name__contains=searched)
        return render(request, 'school/search_schools.html',
                      {'areas': areas, 'info': city_authoschools, 'count': len(city_authoschools),
                       'name_city': city_authoschools[0].city_of_unit})
    if DriverSchoolUnit.objects.filter(city_of_unit__post_code__contains=searched):
        city_autoschools = DriverSchoolUnit.objects.filter(city_of_unit__post_code__contains=searched)
        return render(request, 'school/search_schools.html',
                      {'areas': areas, 'info': city_autoschools, 'count': len(city_autoschools),
                       'name_city': city_autoschools[0].city_of_unit})
    else:
        return render(request, 'school/error404.html')


def search(request):
    if request.GET['searched']:
        searched = request.GET['searched']
        areas = Area.objects.all()
        if DriverSchoolUnit.objects.filter(city_of_unit__name__contains=searched):
            city_authoschools = DriverSchoolUnit.objects.filter(city_of_unit__name__contains=searched)
            return render(request, 'school/search_schools.html',
                          {'areas': areas, 'info': city_authoschools, 'count': len(city_authoschools),
                           'name_city': city_authoschools[0].city_of_unit})
        if DriverSchoolUnit.objects.filter(city_of_unit__post_code__contains=searched):
            city_autoschools = DriverSchoolUnit.objects.filter(city_of_unit__post_code__contains=searched)
            return render(request, 'school/search_schools.html',
                          {'areas': areas, 'info': city_autoschools, 'count': len(city_autoschools),
                           'name_city': city_autoschools[0].city_of_unit})
        else:
            return render(request, 'school/error404.html')


# for big filter
def filtered(request, city):
    areas, schools = Area.objects.all(), DriverSchoolUnit.objects.all()
    filter_value_in_key = {
        "price-low-up": 'cources__price',
        "price-up-low": '-cources__price_id',
        'alphabet': 'driverschool__name',
        'rating': 'driverschool__score',
    }

    letter = request.GET.get('category')
    if request.GET.get('filtered'):
        filtered_schools = DriverSchoolUnit.objects.filter(
            cources__category__name__contains=letter).filter(
            city_of_unit__name__contains=city)
        ordered_schools = filtered_schools.order_by(filter_value_in_key[request.GET.get('filtered')]).distinct(
            filter_value_in_key[request.GET.get('filtered')])

        return render(request, 'school/filtered_schools.html',
                      {'areas': areas, 'filtered_schools': ordered_schools, 'count': len(ordered_schools)})

    else:
        category_filtered = DriverSchoolUnit.objects.filter(
            cources__category__name__contains=letter).filter(
            city_of_unit__name__contains=city)
        return render(request, 'school/filtered_schools.html',
                      {'areas': areas,
                       'filtered_schools': category_filtered, 'count': len(category_filtered)})


# Info about school
def info_about_authoschool(request, school_pk):
    areas, school = Area.objects.all(), get_object_or_404(DriverSchoolUnit, pk=school_pk)
    return render(request, 'school/school_info.html',
                  {'areas': areas, 'school': school})


# just html page
def base(request):
    schools, areas = DriverSchoolUnit.objects.all(), Area.objects.all()
    return render(request, 'school/base.html', {'areas': areas, 'schools': schools})


# just html page
def footer(request):
    areas = Area.objects.all()

    return render(request, 'school/footer.html', {'areas': areas})


# just html page
def error404(request):
    schools, areas = DriverSchoolUnit.objects.all(), Area.objects.all()
    return render(request, 'school/error404.html', {'areas': areas, 'schools': schools})
