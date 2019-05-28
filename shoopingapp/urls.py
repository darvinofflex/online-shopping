from django.urls import path

from . import views

app_name = 'shoopingapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('(?P<product_id>[0-9]+)/', views.detail, name='detail'),
    path('(?P<product_id>[0-9]+)/cancel_order', views.cancel_order, name='cancel_order'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('add_item/', views.add_item, name='add_item'),
]