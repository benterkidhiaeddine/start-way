from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('founders/<int:id>/update', views.founder_update, name='founder_update' ),
    path('founders/<int:id>/detail',views.founder_detail, name ='founder_detail'),
    path('investor_feed' , views.investor_feed, name = 'start_up_list')
    
]