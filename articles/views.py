from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Article, Comments
from django.contrib.auth.decorators import login_required
from . import forms
from django.contrib.auth import get_user_model

# Create your views here.

def article_list(request):
    articles = Article.objects.all().order_by('date')
    writes = Article.objects.all().order_by('date')
    User = get_user_model()
    users = User.objects.all()
    return render(request, 'articles/articles.html', {'articles': articles, 'users':users, 'writes':writes})


def article_detail(request, slug, id):
    article = Article.objects.get(slug=slug)
    comments = Comments.objects.filter(slug=id).order_by('date')
    c_form = forms.CreateComment()
    return render(request, 'articles/article_detail.html', {'article': article, 'comments': comments, 'c_form': c_form})


def likes(request, slug):
    article = Article.objects.get(slug=slug)
    article.likes+=1
    article.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))


@ login_required(login_url='accounts:login')
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('articles:list')
    else:
        form = forms.CreateArticle()
    return render(request, 'articles/new_article.html', {'form': form})


def comments(request, id):
    if request.method == 'POST':
        new = forms.CreateComment(request.POST)
        new_comment = new.save(commit=False)
        new_comment.slug = Article.objects.get(id=id) 
        new_comment.author = request.user
        new_comment.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))


def search(request):
    User = get_user_model()
    users = User.objects.all()
    articles = Article.objects.all().order_by('date')
    writes = Article.objects.all().order_by('date')

    if request.method == 'POST':
        title = request.POST.get('choose')
        search = request.POST.get('search')    

        if title == 'author':
            try:
                user = User.objects.get(username=search)
                articles = Article.objects.filter(author=user.id)
            except:
                articles = Article.objects.all().order_by('date')

        elif title == 'article':
            try:
                articles = Article.objects.filter(title=search)
            except:
                articles = Article.objects.all().order_by('date')

        else:
            articles = Article.objects.all().order_by('date')

    return render(request, 'articles/articles.html', {'writes': writes, 'articles': articles, 'users': users})


def delete(request, id):
    article = Article.objects.get(id=id)
    article.delete()
    return redirect('articles:list')
