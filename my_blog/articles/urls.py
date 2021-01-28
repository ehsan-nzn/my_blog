from django.urls import path
from articles import views

app_name = "articles"
urlpatterns = [
    path("", views.articles_list, name="articles_list"),
    path("<slug>", views.articles_detail, name="articles_detail"),
]
