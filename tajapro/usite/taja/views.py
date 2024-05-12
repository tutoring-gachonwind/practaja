

# Create your views here.
from django.shortcuts import render
import random



def index(request):
    return render(request, 'button.html')

def short_view(request):
    return render(request, 'short.html')

def long_view(request):
    return render(request, 'long.html')




def ranst(request):
    sentences = ["이거 대체 왜 안됨?","함수야 빨리 띄워져라","오늘 점심은 낙곱새","나는 돌"]
    ransen = random.choice(sentences)
    return render(request, 'short.html', {'sentence': ransen})