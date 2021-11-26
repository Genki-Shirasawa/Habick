from django.urls import path
from .views import topfunc, signupfunc, loginfunc, dashboardfunc, \
    logoutfunc, detailfunc, HabitCreate, HabitDelete, HabitUpdate


urlpatterns = [
    path('', topfunc, name='top'),
    path('signup/', signupfunc, name='signup'),
    path('login/', loginfunc, name='login'),
    path('logout/', logoutfunc, name='logout'),
    path('dashboard/', dashboardfunc, name='dashboard'),
    path('create/', HabitCreate.as_view(), name='create'),
    path('detail/<int:pk>', detailfunc, name='detail'),
    path('delete/<int:pk>', HabitDelete.as_view(), name='delete'),
    path('update/<int:pk>', HabitUpdate.as_view(), name='update'),
]
