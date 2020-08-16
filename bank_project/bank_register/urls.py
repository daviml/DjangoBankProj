from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.bank_form,name='bank_insert'), #get and post req for insert
    path('<int:id>/', views.bank_form,name='bank_update'), #get and post req for update
    path('delete/<int:id>/',views.bank_delete,name='bank_delete'),
    path('list/', views.bank_list,name='bank_list') #get and post req for retrieve and display
    
]