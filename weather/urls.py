from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:city_id>', views.delete_block, name = 'delete')
]
