from django.urls import path
from .views import career_chat, get_latest_news

urlpatterns = [
    path("ai/chat/", career_chat, name="career_chat"),
    path("news/latest/", get_latest_news, name="latest_news"),
]
