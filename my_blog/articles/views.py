from django.shortcuts import render, HttpResponse
from articles import models

# Create your views here.
def articles_list(request):
    articles = models.Articles.objects.all().order_by("date")
    args = {"articles": articles}
    return render(request, "articles/articles.html", context=args)


def articles_detail(request, slug):
    # return HttpResponse(slug)
    article = models.Articles.objects.get(slug=slug)
    args = {"article": article}
    return render(request, "articles/articles_detail.html", context=args)
