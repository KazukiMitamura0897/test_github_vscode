from django.urls import path
from .views import IndexView, SentenceView, WordView

urlpatterns = [
    path('', IndexView.as_view()), 
    path('sentence/', SentenceView.as_view()),
    path('word/', WordView.as_view()),
]
