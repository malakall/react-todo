from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView

def news_home(request):
    news = Articles.objects.all()
    # news = Articles.objects.order_by('-date')
    return render(request, 'news/news_home.html', {'news': news})


class NewsDatailView(DetailView):
    model = Articles
    template_name = 'news/details_view.html' # какой шаблон будет обрабатывать вот эту страничку
    context_object_name = 'article' # Ключ по которому мы педаем объект внутрь щаблона


def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')# Если все корректно то сохраняется в нашу базу данных и идет перенапрваление на страницу с урл home
        else:
            error = 'форма была неверной'

    form = ArticlesForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', data)





