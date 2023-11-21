from django.urls import path
from . import views

#urlconfig
urlpatterns = [
    path('',views.Sayora,name="hello")
]