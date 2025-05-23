from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('films/', views.films_index, name='index'),
    path('films/<int:film_id>/', views.films_detail, name='films_detail'),
    path('films/create/', views.FilmCreate.as_view(), name='films_create'),
    path('films/<int:pk>/update/', views.FilmUpdate.as_view(), name='films_update'),
    path('films/<int:pk>/delete/', views.FilmDelete.as_view(), name='films_delete'),
    path('films/<int:film_id>/add_review/', views.add_review, name='add_review'),
    path('accounts/signup/', views.signup, name='signup'),
    path('tags/', views.TagListView.as_view(), name='tags_index'),
    path('tags/<int:pk>/', views.TagDetailView.as_view(), name='tag_detail'),
    path('tags/create/', views.TagCreate.as_view(), name='tag_create'),
    path('tags/<int:pk>/update/', views.TagUpdate.as_view(), name='tag_update'),
    path('tags/<int:pk>/delete/', views.TagDelete.as_view(), name='tag_delete'),
] 