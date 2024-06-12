from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView, CreateView
from django.views.generic.detail import DetailView
from django.views import View
from django.contrib.auth import login
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ImageUploadForm
from .models import Image
from .forms import *
from django.contrib.auth.models import User
from django.http import JsonResponse

class meme_site_register(FormView):
    template_name = 'registration/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(meme_site_register, self).form_valid(form)

class meme_site_login(LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True
    next_page = reverse_lazy('home')

class meme_site_main(ListView):
    model = Image
    template_name = 'home.html'
    paginate_by = 5
    context_object_name = 'images'
    ordering = ['-id']

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Image.objects.filter(title__icontains=query).order_by('-id')
        return Image.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        return context


class meme_site_user_profile(ListView):
    model = Image
    template_name = 'user_profile.html'
    context_object_name = 'images'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs['username'])
        return Image.objects.filter(user=user).order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_profile'] = get_object_or_404(User, username=self.kwargs['username'])
        return context
class meme_site_image_details(DetailView, FormView):
    model = Image
    template_name = 'meme_detail.html'
    context_object_name = 'image'
    form_class = CommentForm
    def get_success_url(self):
        return self.request.path
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.image = self.get_object()
        form.save()
        return super().form_valid(form)
class meme_site_like_image(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        image = get_object_or_404(Image, pk=kwargs['pk'])
        if request.user in image.likes.all():
            image.likes.remove(request.user)
            liked = False
        else:
            image.likes.add(request.user)
            liked = True
        return JsonResponse({'liked': liked, 'likes_count': image.likes.count()})
class meme_site_post_meme(LoginRequiredMixin, CreateView):
    model = Image
    form_class = ImageUploadForm
    template_name = 'upload_meme.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)