from django.urls import path
from . import views
# from django.conf import settings
# from django.conf.urls.static import static


urlpatterns = [

    path('', views.home1, name='home1'),
    path('login/', views.handlelogin, name='login'),
    path('logout/', views.handlelogout, name='logout'),
    path('subscribe/', views.subscribe, name='subscribe'),

    path('addgram/', views.addgram, name='addgram'),
    path('viewgram/', views.viewgram, name='viewgram'),
    path('updateGrampanchayat/<int:pk>/', views.updateGrampanchayat, name='updateGrampanchayat'),
    path('gramdetail/<int:pk>/', views.gramdetail, name='gramdetail'),
    path('deletegram/<int:pk>/', views.deletegram, name='deletegram'),

    path('addgramadmin/<int:pk>/', views.addgramadmin, name='addgramadmin'),
    path('viewgramadmin/<int:pk>/', views.viewGramAdmin, name='viewgramadmin'),
    path('deletegramadmin/<int:pk>/', views.deletegramadmin, name='deletegramadmin'),

    path('addBirthDetails/', views.addBirthDetails, name='addBirthDetails'),
    path('requestbirthcertificate/', views.requestBirthCertificate, name='requestbirthcertificate'),

    path('addAuthority/', views.addAuthority, name='addAuthority'),
    path('addComplaint/', views.addComplaint, name='addComplaint'),

    path('addfamilyhead/', views.addFamilyHead, name='addfamilyhead'),
    path('addFamilymember/', views.addFamilymember, name='addFamilymember'),
    path('viewFamily/', views.viewFamily, name='viewFamily'),
    path('viewFamilyDetails/<int:pk>/', views.viewFamilyDetails, name='viewFamilyDetails'),

    path('addScheme/', views.addScheme, name='addScheme'),

    path('addWaterConnection/', views.addWaterConnection, name='addWaterConnection'),
    path('addWaterTax/', views.addWaterTax, name='addWaterTax'),
    path('viewWaterConnections/', views.viewWaterConnections, name='viewWaterConnections'),
    path('waterConnectionDetails/', views.waterConnectionDetails, name='waterConnectionDetails'),
    path('viewWaterTax/<int:pk>/', views.viewWaterTax, name='viewWaterTax'),

    path('addHousetax/', views.addHousetax, name='addHousetax'),
    path('addHouse/', views.addHouse, name='addHouse'),
    path('viewHouses/', views.viewHouses, name='viewHouses'),
    path('houseDetails/', views.houseDetails, name='houseDetails'),
    path('viewhousetax/<int:pk>/', views.viewHouseTax, name='viewhousetax'),

    path('addNotice/', views.addNotice, name='addNotice'),
    path('viewNotice/', views.viewNotice, name='viewNotice'),

    path('addScheme/', views.addScheme, name='addScheme'),
    path('viewScheme/', views.viewScheme, name='viewScheme'),
    path('applySeheme/<int:pk>/', views.applyScheme, name='applyScheme'),

]