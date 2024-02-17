
from django.contrib import admin
from django.urls import path
from todoApp.views import home , LoginPage , SignupPage , add_todo , signout , delete_todo,edit_todo, change_todo,onboarding


urlpatterns = [
   path('' , home , name='home' ), 
   path('signup/',SignupPage,name='signup'),
   path('login/',LoginPage,name='login'),
   path('onboarding/', onboarding, name='onboarding'),
   path('add-todo/' , add_todo ), 
   path('delete-todo/<int:id>' , delete_todo ),
   path('edit-todo/<int:id>/', edit_todo, name='edit_todo'),
 
   path('change-status/<int:id>/<str:status>' , change_todo ), 
   path('logout/' , signout ), 
]
