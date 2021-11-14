from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import logout
from .models import *
from .forms import *
# Create your views here.
menu = [{'title': "Абонементи", 'url_name': "home"},
        {'title': "Тренери", 'url_name': "trainers"},
        {'title': "Добавити себе як тренера", 'url_name': "add_trainer"}]


def logout_user(request):
    logout(request)
    return redirect('home')

def abonements(request):
    form = Abonement.objects.all()
    return render(request, 'gym/abonements.html', {'form': form, 'menu': menu})

def trainers(request):
    form = Trainer.objects.all()
    return render(request, 'gym/trainers.html', {'form': form, 'menu': menu})

def members(request):
    return render(request, 'gym/members.html', {'menu': menu})

def add_trainer(request):
    if request.method == 'POST':
        form = AddTreanerForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            try:
                new_post = form.save(commit=False)
                new_post.name = request.user.first_name
                print(request.user.first_name)
                new_post.surname = request.user.last_name  
                new_post.save()
                return redirect('home')
            except:
                form.add_error(None, 'Ошибка добавления поста')
    else:
        form = AddTreanerForm()
    return render(request, 'gym/add_trainer.html', {'form': form, 'menu': menu})

