from django.urls import path, re_path

from .views import abonements, logout_user, trainers, members, add_trainer


urlpatterns = [
    path('' , abonements, name='home'),
    path('trainers/', trainers , name='trainers'),
    path('members/', members, name='members'),
    path('add_trainer/', add_trainer, name='add_trainer'),
    path('logout/', logout_user, name='logout')
]


