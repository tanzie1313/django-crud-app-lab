from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Film, Review, Tag
from django import forms

class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ['title', 'director', 'queer_themes', 'rating', 'where_to_watch', 'tags']
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text', 'stars', 'date_watched']

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'main_app/about.html')

@login_required
def films_index(request):
    films = Film.objects.filter(owner=request.user)
    return render(request, 'films/index.html', { 'films': films })

@login_required
def films_detail(request, film_id):
    film = Film.objects.get(id=film_id)
    review_form = ReviewForm()
    return render(request, 'films/detail.html', {
        'film': film,
        'review_form': review_form
    })

@login_required
def add_review(request, film_id):
    form = ReviewForm(request.POST)
    if form.is_valid():
        new_review = form.save(commit=False)
        new_review.film_id = film_id
        new_review.user = request.user
        new_review.save()
    return redirect('films_detail', film_id=film_id)

class FilmCreate(LoginRequiredMixin, CreateView):
    model = Film
    form_class = FilmForm

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class FilmUpdate(LoginRequiredMixin, UpdateView):
    model = Film
    form_class = FilmForm

class FilmDelete(LoginRequiredMixin, DeleteView):
    model = Film
    success_url = '/films/'

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

# Tag CRUD views
class TagListView(ListView):
    model = Tag
    template_name = 'main_app/tags/index.html'
    context_object_name = 'tags'

class TagDetailView(DetailView):
    model = Tag
    template_name = 'main_app/tags/detail.html'
    context_object_name = 'tag'

class TagCreate(CreateView):
    model = Tag
    fields = ['name']
    template_name = 'main_app/tags/tag_form.html'
    success_url = '/tags/'

class TagUpdate(UpdateView):
    model = Tag
    fields = ['name']
    template_name = 'main_app/tags/tag_form.html'
    success_url = '/tags/'

class TagDelete(DeleteView):
    model = Tag
    template_name = 'main_app/tags/tag_confirm_delete.html'
    success_url = '/tags/'
