from django.urls import path
from . import auth
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.home, name="home"),
    path('login/', auth.user_login, name='login'),
    path('signup/', auth.user_signup, name='signup'),
    path('logout/', auth.user_logout, name='logout'),
    path('founders/<int:id>/update', views.founder_update, name='founder_update' ),
    path('founders/<int:id>/detail',views.founder_detail, name ='founder_detail'),
    path('employees/<int:id>/detail',views.employee_detail, name ='employee_detail'),
    path('employees/<int:id>/update',views.employee_update, name ='employee_update'),
    path('investor_feed' , views.investor_feed, name = 'start_up_list')
    
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



