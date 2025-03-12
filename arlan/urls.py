from django.urls import path
from .views import home, vacancies_list, vacancy_detail

urlpatterns = [
    path('', home, name='home'),  
    path('vacancies/', vacancies_list, name='vacancies_list'),
    path('vacancies/<int:id>/', vacancy_detail, name='vacancy_detail'),
]
