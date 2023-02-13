
from django.urls import path
from . import views

urlpatterns = [

    path('', views.home1, name='home1'),
    path('login/', views.handlelogin, name='login'),
    path('logout/', views.handlelogout, name='logout'),
    path('addGram/', views.addGram, name='addGram'),
    path('addAdmin/', views.addAdmin, name='addAdmin'),
    path('addFamily/', views.addFamily, name='addFamily'),
    path('addFamilymember/', views.addFamilymember, name='addFamilymember'),
    path('addHouse/', views.addHouse, name='addHouse'),
    path('addAuthority/', views.addAuthority, name='addAuthority'),
    path('addSpot/', views.addSpot, name='addSpot'),
    path('addHousetax/', views.addHousetax, name='addHousetax'),
    path('addWateratax/', views.addWatertax, name='addWatertax'),
    path('Waterconnectioninfo/', views.Waterconnectioninfo, name='Waterconnectioninfo'),
    path('addRoad/', views.addRoad, name='addRoad'),
    path('addScheme/', views.addScheme, name='addScheme'),
    path('addBirthinfo/', views.addBirthinfo, name='addBirthinfo'),
    path('addMarriageinfo/', views.addMarriageinfo, name='addMarriageinfo'),
    path('addComplaint/', views.addComplaint, name='addComplaint'),
]