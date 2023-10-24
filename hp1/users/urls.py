from django.urls import path
from . import views

urlpatterns = [

                path('login/', views.loginUser, name='login'),
                path('logout/', views.logoutUser, name='logout'),
                path('register/', views.registerUser, name='register'),
                path('account/', views.userAccount, name='account'),

                path('add-skill/', views.addskill, name='add-skill'),
                path('update-skill/<str:pk>', views.updateskill, name='update-skill'),
                path('delete-skill/<str:pk>', views.deleteskill, name='delete-skill'),

                path('editaccount/', views.editaccount, name='edit-account'),
                #path('update-profile/<str:pk>', views.updateprofile, name='update-profile'),
                #
                #path('delete-profile/<str:pk>', views.deleteprofile, name='delete-profile'),

                path('', views.profiles, name='profiles'),
                path('profiles/<str:p>/',views.userprofile, name='user-profile'),
]