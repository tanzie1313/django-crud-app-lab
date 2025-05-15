"""
URL configuration for queerfilmapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('films/', views.films_index, name='index'),
    path('films/<int:film_id>/', views.films_detail, name='films_detail'),
    path('films/create/', views.FilmCreate.as_view(), name='films_create'),
    path('films/<int:pk>/update/', views.FilmUpdate.as_view(), name='films_update'),
    path('films/<int:pk>/delete/', views.FilmDelete.as_view(), name='films_delete'),
    path('films/<int:film_id>/add_review/', views.add_review, name='add_review'),
    path('accounts/signup/', views.signup, name='signup'),
]
