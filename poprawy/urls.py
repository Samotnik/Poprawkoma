from django.urls import path

from . import views

urlpatterns = [
    path('uczen/', views.uczenPage, name='uczen_page'),
    path('', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('pomoc/', views.pomoc, name='pomoc'),
    path('nauczyciel/', views.nauczycielPage, name='nauczyciel_page')
]