from django.shortcuts import render, get_object_or_404
from .models import Vacancy

def home(request):
    return render(request, 'home.html')

def vacancies_list(request):
    vacancies = Vacancy.objects.all()
    return render(request, "post_list.html", {"vacancies": vacancies})

def vacancy_detail(request, id):
    vacancy = get_object_or_404(Vacancy, id=id)  # Исправлено
    return render(request, "vacancy_detail.html", {"vacancy": vacancy})
