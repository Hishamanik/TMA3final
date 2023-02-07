from django.urls import path, include
from part2 import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/', include('part2.api.urls'))
]