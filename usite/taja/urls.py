from django.contrib import admin
from django.urls import path
from taja import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.index, name='index'),  # 기본 페이지
    path('short/', views.short_view, name='short'),  # 짧은 글 페이지
    path('long/', views.long_view, name='long'),  # 긴 글 페이지
    path('get-random-sentence/', views.get_random_sentence, name='get_random_sentence'),
    path('check-sentence/', views.check_sentence, name='check_sentence'),
    path('get-random-sentence2/', views.get_random_sentence2, name='get_random_sentence2'),
]