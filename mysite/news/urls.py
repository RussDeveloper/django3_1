from django.urls import path
from news.views import *

urlpatterns = [

    path('news/<int:news_id>', view_news, name='view_news'),
]




