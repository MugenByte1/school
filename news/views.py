from django.shortcuts import render, get_object_or_404, redirect
from .models import News
from django.contrib.auth.decorators import login_required
from .forms import NewsForm

def news_list(request):
    news_items = News.objects.all().order_by('-created_at')
    return render(request, 'news/news_list.html', {'news_items': news_items})

def news_detail(request, id):
    news = get_object_or_404(News, id=id)
    return render(request, 'news/news_detail.html', {'news': news})


@login_required
def news_add(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('news:news_list')
    else:
        form = NewsForm()
    return render(request, 'news/news_form.html', {'form': form})



def news_edit(request, pk):
    news = News.objects.get(pk=pk)
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES, instance=news)
        if form.is_valid():
            form.save()
            return redirect('news:news_list')
    else:
        form = NewsForm(instance=news)
    return render(request, 'news/news_form.html', {'form': form})

def news_delete(request, pk):
    news = News.objects.get(pk=pk)
    if request.method == 'POST':
        news.delete()
        return redirect('news:news_list')
    return render(request, 'news/news_confirm_delete.html', {'news': news})
