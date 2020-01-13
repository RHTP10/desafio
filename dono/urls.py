from django.urls import path
from dono.views import *

urlpatterns = [
    path('cadastro/', cadastro),
    path('delete/<int:id>', delete),
    path('update/<int:id>', update),
]

