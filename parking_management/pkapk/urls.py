from django.urls import path
from .views import showallservices
from pkapk import views

urlpatterns = [
    path('showvehicle',views.showallservices, name='showvehicle'),
    path('edit/', views.edit, name='edit'),
    path('deletevehicle/<int:pk>', views.deletevehicle, name='deletevehicle'),
    path('vadd/', views.addvehicle, name='vadd'),
    path('update/<int:id>/', views.update, name='update'),

    path('activate_item/<int:item_id>/', views.activate_item, name='activate_item'),
    path('deactivate_item/<int:item_id>/', views.deactivate_item, name='deactivate_item'),

    path('vehicle_entry/', views.vehicleentry, name='vehicle_entry'),
    path('addvehicle/', views.addvehicle_entry, name='addvehicle'),

    path('', views.dashboard, name='dashboard'),
    path('addcategory',views.addcategory,name='addcategory'),

    path('managevehicle/', views.managevehicle, name='managevehicle'),

    path('searchvehicle/', views.search, name='searchvehicle'),

    path('c_password', views.c_password, name='c_password'),

    path('Category/togglestatus/<int:item_id>/', views.togglestatus, name='togglestatus'),
    path('accountsetting', views.accountsetting, name='accountsetting'),
    # path('change_password/', views.change_password, name='change_password'),
    path('report',views.report,name='report')

]

