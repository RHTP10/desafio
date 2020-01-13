
from django.contrib import admin
from django.urls import path, include

from gatinho.views import *
import dono.urls

urlpatterns = [
    path('', home),
    path('dono/', include('dono.urls')),
    path('detail/<int:id>', detail),
    path('delete/<int:id>', delete),
    path('update/<int:id>', update),
    path('admin/', admin.site.urls),
]
