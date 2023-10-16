from django.shortcuts import render
from Admin_dashboard.models import NewsArticle
from django.shortcuts import render, get_object_or_404
# Create your views here.
def blog(request):
   news_articles = NewsArticle.objects.all()
   return render(request, 'index.html', {'news_articles': news_articles})
def detail(request, article_id):
    article = get_object_or_404(NewsArticle, pk=article_id)
    return render(request, 'details.html', {'article': article})