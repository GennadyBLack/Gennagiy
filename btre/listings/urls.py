from django.urls import path
from .views import *

urlpatterns = [
    path('',listings,name='listings'),
    path('<int:id>/',listing,name='listing'),
    path('search/',search,name='search')
]
