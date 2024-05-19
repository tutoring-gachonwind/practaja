

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
import random



def index(request):
    return render(request, 'button.html')

def short_view(request):
    return render(request, 'short.html')

def long_view(request):
    return render(request, 'long.html')

sentences = [
        "지금까지의 여정이 많은 것을 가르쳐 주었습니다.",
        "먼저 일어나고 열심히 일하는 것이 성공의 비결입니다.",
        "지식을 쌓고 경험을 쌓아서 더 나은 미래를 준비하세요.",
        "새로운 연구 결과에 따르면 정기적인 운동이 심장 건강에 크게 도움이 됩니다.",
        "그녀는 매일 아침 일찍 일어나서 조깅을 하는 것을 좋아합니다.",
        "최근 발표된 보고서는 기후 변화의 심각성을 경고하고 있습니다.",
        "우리는 이번 여름에 가족과 함께 해변으로 여행을 갈 계획입니다.",
        "회의 중에 다양한 아이디어가 나왔지만 결론을 내리기에는 시간이 부족했습니다.",
        "그의 유머 감각은 언제나 우리를 웃게 만들었습니다.",
        "이 도시는 역사적인 건축물과 현대적인 시설이 조화를 이루고 있습니다.",
        "새로운 소프트웨어 업데이트는 사용자 인터페이스를 더욱 직관적으로 만들었습니다.",
        "그녀는 친구들에게서 많은 생일 축하 메시지를 받았습니다.",
        "이 요리는 다양한 재료가 어우러져 독특한 맛을 냅니다.",
]

sentences2 = [ "어느 한 작은 마을에 푸른 바다가 바라보이는 언덕 위에 자리 잡은 오래된 집이 있었습니다. 그 집은 세월의 흔적을 고스란히 간직한 채로, 지나가는 바람과 햇살을 맞이하며 조용히 서 있었습니다. 집 주인인 할아버지는 매일 아침 일찍 일어나 집 주변을 돌며 정원을 가꾸고, 고양이 두 마리와 함께 평화로운 일상을 보냈습니다. 그의 하루는 느긋하고 차분하게 흘러갔고, 마을 사람들은 할아버지를 매우 존경했습니다. 할아버지는 가끔씩 마을 아이들에게 옛날 이야기를 들려주곤 했는데, 아이들은 그 이야기 속에서 상상력을 키우며 즐거워했습니다. 할아버지의 이야기는 언제나 교훈과 따뜻함이 가득하여 듣는 이들에게 큰 감동을 주었습니다. 그렇게 시간이 흘러가고, 어느덧 많은 계절이 지나갔지만 할아버지의 일상은 변함이 없었습니다. 그는 여전히 그 집에서 행복한 시간을 보내며, 지나가는 이들에게 잔잔한 미소를 선사했습니다. 푸른 바다와 함께하는 그 집은 할아버지의 삶을 담은 작은 천국이었습니다.",
"가을이 깊어가는 어느 날, 작은 마을에 새로 이사 온 가족이 있었습니다. 이 가족은 도시의 복잡한 생활을 떠나 평화로운 시골에서 새로운 시작을 꿈꾸며 이곳에 왔습니다. 집 주변은 울긋불긋 물든 나무들로 둘러싸여 있었고, 맑은 공기와 청명한 하늘이 그들을 반겼습니다. 아침이면 새들의 노랫소리가 창문을 통해 들려왔고, 저녁이면 붉게 물든 노을이 지평선을 물들였습니다. 가족은 마을 사람들과 빠르게 친해졌고, 함께 농사를 짓고 축제를 준비하며 즐거운 시간을 보냈습니다. 아이들은 마을 친구들과 어울려 들판을 뛰어다니며 행복한 시간을 보냈고, 부모님은 집안일을 나누어 하며 서로의 사랑을 다시금 확인할 수 있었습니다. 이 가족의 새로운 삶은 단순했지만, 그 단순함 속에서 진정한 행복을 찾을 수 있었습니다. 매일매일이 감사와 기쁨으로 가득한 날들이었습니다. 그들은 이곳에서 오래도록 행복하게 살기를 꿈꾸며, 오늘도 서로를 위해 최선을 다하고 있습니다.",
               ]

def short_view(request):
    random_sentence = random.choice(sentences)
    return render(request, 'short.html', {'random_sentence': random_sentence})

def long_view(request):
    random_sentence = random.choice(sentences2)
    return render(request, 'long.html', {'random_sentence': random_sentence})


def get_random_sentence(request):
    random_sentence = random.choice(sentences)
    return JsonResponse({'random_sentence': random_sentence})


def get_random_sentence2(request):
    random_sentence = random.choice(sentences2)
    return JsonResponse({'random_sentence': random_sentence})


def check_sentence(request):
    if request.method == 'POST':
        user_sentence = request.POST.get('user_sentence', '')
        random_sentence = request.POST.get('random_sentence', '')

        is_correct = (user_sentence.strip() == random_sentence.strip())
        correct_chars = sum(1 for a, b in zip(user_sentence, random_sentence) if a == b)

        response_data = {
            'is_correct': is_correct,
            'correct_chars': correct_chars
        }
        return JsonResponse(response_data)
    else:
        return short_view(request)

