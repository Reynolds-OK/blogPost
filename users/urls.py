from django.urls import path
from . import views

app_name = 'profile'

urlpatterns = [
    path('<username>/<int:id>/', views.user_profile, name="user_profile"),
    path('<int:id>/', views.password, name="password"),   
]
