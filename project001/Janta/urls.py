from django.urls import path
from . import views

urlpatterns = [
    path('', views.managerlogin, name='login'),
    path('createmanager/', views.createmanager, name='managers'),
    path('updatemanager/<str:pk>/', views.updatemanager, name='update_managers'),
    path('deletemanager/<str:pk>/', views.deletemanager, name='delete_managers'),
    path('managerprofile/', views.managerprofile, name='manager_profile'),

    path('jantaorders/', views.allorders, name='janta_orders'),
    path('jantareports/', views.jantareports, name='janta_reports'),

    path('createwriter/', views.createwriter, name='writers'),
    path('updatewriter/<str:pk>/', views.updatewriter, name='update_writers'),
    path('deletewriter/<str:pk>/', views.deletewriter, name='delete_writers'),

    path('logout/', views.managerlogout, name='logout'),
    path('dashboard/', views.managerdashboard, name='managerdashboard'),

    path('addorder/', views.addorder, name='add_order'),
    path('editorder/<str:pk>/', views.editorder, name='edit_order'),
    path('deleteorder/<str:pk>/', views.deleteorder, name='delete_order'),

    path('jantaadmin/', views.jantadashboard, name='dashboard'),

    path('exportcsv/', views.export_csv, name='export_csv'),
]