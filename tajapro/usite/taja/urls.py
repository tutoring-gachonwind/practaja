from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # 기본 페이지
    path('short/', views.short_view, name='short'),  # 짧은 글 페이지
    path('long/', views.long_view, name='long'),  # 긴 글 페이지
    path('ranst/', views.ranst, name='ranst'),
]