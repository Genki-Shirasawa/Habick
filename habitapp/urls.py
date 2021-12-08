from django.urls import path
from . import views


app_name = 'habitapp'
urlpatterns = [
    path('', views.topfunc, name='top'),
    path('signup/', views.signupfunc, name='signup'),
    path('login/', views.loginfunc, name='login'),
    path('logout/', views.logoutfunc, name='logout'),
    path('dashboard/', views.dashboardfunc, name='dashboard'),
    path('create/', views.HabitCreate.as_view(), name='create'),
    path('detail/<int:pk>', views.detailfunc, name='detail'),
    path('delete/<int:pk>', views.HabitDelete.as_view(), name='delete'),
    path('update/<int:pk>', views.HabitUpdate.as_view(), name='update'),
]
