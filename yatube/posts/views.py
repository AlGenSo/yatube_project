from django.shortcuts import render
from django.http import HttpResponse

# Create views.
def index(request):
    return HttpResponse('Главная страница')

def groups_posts(request, slug):
    return HttpResponse(f'Темы постов {slug}')
