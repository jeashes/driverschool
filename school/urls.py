from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # Home
    path('', views.home, name='home'),

    # Info about school
    path('search/', views.Search.home_search, name='search'),
    path('search/<str:searched>', views.Search.main_search, name='search_authoschool'),

    # Search on city/city_code/name and area
    path('school/<int:school_pk>', views.info_about_authoschool, name='view_school'),

    # Filter on category/price/letters/score
    path('filtered/<str:city>', views.Filter.main_filter, name='filtered'),

    # header + footer
    path('base', views.base, name='base'),
    path('footer', views.footer, name='footer'),

    # error404
    path('error404', views.error404, name='error404'),

    # forms
    path('create_driver_app', views.Application.create_driver_application, name='driver_app'),
    path('create_partnership_app', views.Application.create_partnership_app, name='partnership_app')

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
