from django.urls import path
from .views import Abdurashid, Abdushukur, Maftuna, Mokhinur, Muhammad, Mukaddam, Samandar, index, about, asd, Nasriddin, Muhammadali
Muhammad, Mukaddam, Mokhinur, Maftuna, Abdushukur, Abdurashid, Samandar

urlpatterns = [
    path('', index),
    path('about/', about),
    path('asd/', asd),
    path('Muhammadali/', Muhammadali),
    path('Nasriddin/', Nasriddin),
    path('Abdushukur/', Abdushukur),
    path('Samandar/', Samandar),
    path('Abdurashid/', Abdurashid),
    path('Muhammad/', Muhammad),
    path('Mukaddam/', Mukaddam),
    path('Mokhinur/', Mokhinur),
    path('Maftuna/', Maftuna),
]
