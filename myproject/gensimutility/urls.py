from django.urls import path
from App import views

urlpatterns = [
    path('overview/',views.Overview,name='Overview'),
    path('',views.Main , name='Main'),
    path('dataset/',views.dataset,name='dataset'),
    path('home/',views.home,name='home'),
    path('login/',views.login,name='login'),
        
]
    