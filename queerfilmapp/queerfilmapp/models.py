from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Film(models.Model):
    title = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    queer_themes = models.TextField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 11)])
    where_to_watch = models.URLField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('films_detail', kwargs={'film_id': self.id})

class Review(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    stars = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    date_watched = models.DateField()

    def __str__(self):
        return f"{self.user.username}'s review of {self.film.title}"

    class Meta:
        unique_together = ('film', 'user')  # Ensures one review per user per film 