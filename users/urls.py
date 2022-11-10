from storage.views import Contact_form
from django.urls import path,include

from .views import DashboardListView,register,index,about,team

urlpatterns = [
    path('dashboard/',DashboardListView.as_view(),name='dashboard'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('register/',register,name='register'),
    path('oauth/',include('social_django.urls')),
    path('',index,name='index'),
    path('about/',about,name='about'),
    path('team/',team,name='team'),
   
    # path('contact/',Contact_form,name='contact'),
]