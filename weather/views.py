import requests
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import City
from .forms import CityForm

def index(request):
  appid = 'fa595220fcc627ebaed212eac34747cf'
  url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

  if (request.method == 'POST'):
    form = CityForm(request.POST)
    form.save()

  form = CityForm()

  cities = City.objects.all()

  all_cities = []

  for city in cities:
    res = requests.get(url.format(city.name)).json()
    city_info = {
      'city': city.name,
      'temp': res["main"]["temp"],
      'icon': res["weather"][0]["icon"],
      'id': city.id
    }

    all_cities.append(city_info)

  context = {'all_info': all_cities, 'form': form}

  return render(request  , 'weather/index.html', context )

def delete_block(request, city_id):
  try:
    city = City.objects.get(id = city_id)
  except:
    raise Http404('Город не найден')

  city.delete()

  return HttpResponseRedirect( reverse('index') )
