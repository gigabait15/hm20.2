from django.urls import path

from main.views import home, contact

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contact, name='contact')
]