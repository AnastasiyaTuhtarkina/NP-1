from django.urls import path
from .views import *


urlpatterns = [
    path('', PostList.as_view()),
    path('', PostDetail.as_view(), name='post'),
]