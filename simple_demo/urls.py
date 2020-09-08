from django.contrib import admin
from django.urls import path
from first_app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('team_name_url/', views.home),
    path('view_database/', views.view_database),
    path('signup/', views.signup),
    path('sign_insert/', views.sign_insert),

]
