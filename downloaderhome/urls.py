from django.urls import path
from downloaderhome.views import home


urlpatterns = [
    path('', home, name='home'),
]