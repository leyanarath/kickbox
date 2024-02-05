from django.urls import path
from . import views

urlpatterns = [
   
     path('',views.fun1,name='fun1'),
     # path('about/',views.about,name='about'),
     path('reg/',views.register,name='register'),
     path('login/',views.login,name="login"),
     path('logout/',views.logout,name='logout'),
]