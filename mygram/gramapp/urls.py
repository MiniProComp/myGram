from django.urls import path
from . import views
# from django.conf import settings
# from django.conf.urls.static import static
from .views import GeneratePdf

urlpatterns = [

    path('', views.home1, name='home1'),
    path('login/', views.handlelogin, name='login'),
    path('logout/', views.handlelogout, name='logout'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('addgram/', views.addgram, name='addgram'),
    path('viewgram/', views.viewgram, name='viewgram'),
    path('gramdetail/<int:pk>/', views.gramdetail, name='gramdetail'),
    path('deletegram/<int:pk>/', views.deletegram, name='deletegram'),
    path('addgramadmin/<int:pk>/', views.addgramadmin, name='addgramadmin'),
    path('viewgramadmin/<int:pk>/', views.viewGramAdmin, name='viewgramadmin'),
    path('deletegramadmin/<int:pk>/', views.deletegramadmin, name='deletegramadmin'),

    path('addBirthDetails/', views.addBirthDetails, name='addBirthDetails'),
    path('requestbirthcertificate/', views.requestBirthCertificate, name='requestbirthcertificate'),
    path('pdf/', GeneratePdf.as_view(), name='pdf'),

    path('addAuthority/', views.addAuthority, name='addAuthority'),
    path('addComplaint/', views.addComplaint, name='addComplaint'),
    path('addfamilyhead/', views.addFamilyHead, name='addfamilyhead'),
    path('addFamilymember/', views.addFamilymember, name='addFamilymember'),

    path('addScheme/', views.addScheme, name='addScheme'),
    path('waterConnectioninfo/', views.waterConnectioninfo, name='waterConnectioninfo'),
    path('addWatertax/', views.addWatertax, name='addWatertax'),

    path('addHousetax/', views.addHousetax, name='addHousetax'),
    path('addHouse/', views.addHouse, name='addHouse'),
    path('houseDetails/', views.houseDetails, name='houseDetails'),
    path('viewhousetax/<int:pk>/', views.viewHouseTax, name='viewhousetax'),

    path('viewFamily/', views.viewFamily, name='viewFamily'),
    path('viewFamilyDetails/<int:pk>/', views.viewFamilyDetails, name='viewFamilyDetails'),

]