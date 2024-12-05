from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('upload/', views.upload, name="upload"),
    path('watch/<int:id>', views.watch, name="watch"),
    path('react/', views.react, name="react"),
    path('comment/', views.comment, name="comment"),

]