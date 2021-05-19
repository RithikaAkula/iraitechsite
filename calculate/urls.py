from . import views as user_views

from django.urls import path,include

urlpatterns = [

    path('', user_views.index, name='index'),
    path('result/', user_views.calculate, name='result'),
]