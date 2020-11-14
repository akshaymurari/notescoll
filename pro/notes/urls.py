from django.urls import path
from . import views
urlpatterns = [
    path('',views.fun,name="home"),
    path('save',views.save,name="save"),
    path('dele',views.dele,name="dele"),
]