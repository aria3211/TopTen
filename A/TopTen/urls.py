from django.urls import path
from . import views

urlpatterns = [
    path('', views.show,name="home"),
    path('movie/<str:Top_title>/',views.show_movie,name="Movie"),
    path('test/',views.test)

]
