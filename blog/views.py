from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from  .forms import BlogpostForm, UserForm
from . models import Blogpost
def index(request):
    if not request.user.is_authenticated:
        return render(request, 'blog/login.html')
    else:
        blogposts = Blogpost.objects.filter(user=request.user)
        query = request.GET.get("q")
        if query:
            blogposts = blogposts.filter(
                Q(blogpost_title__icontains=query) |
                Q(content__icontains=query)
            ).distinct()
            return render(request, 'blog/index.html', {
                'blogposts': blogposts,

            })
        else:
            return render(request, 'blog/index.html', {'blogposts': blogposts})

def detail(request,blogpost_id):
    if not request.user.is_authenticated:
        return render(request, 'blog/login.html')
    else:
        blogpost = get_object_or_404(Blogpost, pk=blogpost_id)
        return render(request, 'blog/detail.html', {'blogpost': blogpost})

def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                problemsets = Problemset.objects.filter(user=request.user)
                return render(request, 'blog/index.html', {'blogposts': blogposts})
    context = {
        "form": form,
    }
    return render(request, 'blog/register.html', context)

def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'blog/login.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                blogposts = Blogpost.objects.filter(user=request.user)
                return render(request, 'blog/index.html', {'blogposts': blogposts})
            else:
                return render(request, 'blog/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'blog/login.html', {'error_message': 'Invalid login'})
    return render(request, 'blog/login.html')


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                blogposts = Blogpost.objects.filter(user=request.user)
                return render(request, 'blog/index.html', {'blogposts': blogposts})
    context = {
        "form": form,
    }
    return render(request, 'blog/register.html', context)

def create_blogpost(request):
    if not request.user.is_authenticated:
        return render(request, 'blog/login.html')
    else:
        form = BlogpostForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            blogpost = form.save(commit=False)
            blogpost.user = request.user


            blogpost.save()
            return render(request, 'blog/detail.html', {'blogpost': blogpost})
        context = {
            "form": form,
        }
        return render(request, 'blog/create_blogpost.html', context)