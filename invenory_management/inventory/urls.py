from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^aboutme$', aboutme, name='aboutme'),
    url(r'^meetpups$', meetpups, name='meetpups'), 
    url(r'^display_pup$', display_pup, name='display_pup'),
    url(r'^menu$', menu, name='menu'),
    url(r'^reservations$', reservations, name='reservations'),
    url(r'^contact$', contact, name='contact'),


    #url(r'^$', index, name='calendar'),
    #url(r'^resturant$', display_resturant, name="display_resturant")
    

]

