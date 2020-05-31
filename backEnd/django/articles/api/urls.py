from django.urls import path

from .view import (
    ArticleListView, 
    ArticleDetailView,
    ArticleCreateView,
    ArticleUpdateView,
)

urlpatterns = [
    path('', ArticleListView.as_view()),
    path('<pk>', ArticleDetailView.as_view()),
    path('<pk>/update', ArticleUpdateView.as_view()),
    path('create/', ArticleCreateView.as_view())
]



