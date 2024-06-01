# Practaja
  
***2024-1 튜터링 개인 텀프로젝트 - 타자 연습이 가능한 사이트 구현하기 (개발 기간 : 3주일)***

**개발 목적 : 자투리 시간을 활용하여 타자연습을 할 수 있는 사이트를 제작하여 타자 실력 향상을 위함**
--------

### 프로젝 실행 방법

http://127.0.0.1:8000/taja/ 링크를 통해 접속한다

--------

### 프로그램 설명 

사이트 이동 시 메인화면에 짧은 글 , 긴 글 을 선택하는 버튼이 나타남
2) 짧은 글 선택시 랜덤한 문장들이 나오며 총 5번을 진행 → 진행 후 정확도, 타자율 확인 가능하며 재진행 or 메인화면 돌아가기 선택 가능
3) 긴 글 선택한 랜덤한 문장이 나오며 총 1번 진행 → 진행 후 정확도, 타자율 확인 가능하며 재진행 or 메인화면 돌아가기 선택 가능

--------

### 사용 라이브러리 및 테크  

* 테크 :
  * PyCharm Community Edition 2024.1.1
 
* 라이브러리 사용 X 

--------

### 1주차 : 프로젝트 기획
https://github.com/tutoring-gachonwind/practaja/tree/main/tajapro/usite
- HTML,CSS Django 학습
- Django 프로젝트 구현하여 가상 환경에 프로젝트를 만들고 HTML을 이용하여 짧은글, 긴글로 연결하게 만드는 홈사이트 구축

-------  

### 2단계 : 기능 구현  
https://github.com/tutoring-gachonwind/practaja/tree/main/usite
- 짧은 글을 누르면 랜덤한 리스트에서 문장들이 나오고 그 문장을 입력하면 내가 입력한 문장과 원래 문장이 나오며 알맞게 입력했으면 맞았습니다 라는 문구가, 다르게 입력했을 경우 틀렸습니다 라는 문구가 나오고 정확도와 타자율이 나오도록 구현
- 짧은 글은 5번을 한 세트로 적용하여 5번을 입력하면 다시 시도하겠냐는 팝업이 뜨면서 예를 누르면 다시 시도하고 취소를 눌렀을 경우 홈으로 다시 돌아가도록 구현
- 긴 글 누르면 랜덤한 리스트에서 문장들이 나오고 그 문장을 입력하면 내가 입력한 문장과 원래 문장이 나오며 알맞게 입력했으면 맞았습니다 라는 문구가, 다르게 입력했을 경우 틀렸습니다 라는 문구가 나오고 정확도와 타자율이 나오도록 구현
- 긴 글은 1번을 한 세트로 적용하여 모두 입력하면 다시 시도하겠냐는 팝업이 뜨면서 예를 누르면 다시 시도하고 취소를 눌렀을 경우 홈으로 다시 돌아가도록 구현

-------

### 3단계 : 기능 구현 및 사이트 스타일 정리  
- 내가 입력한 문장과 제시된 문장이 다를 경우 다른 부분을 빨간색과 굵게 스타일을 넣어 내가 어느부분을 다르게 입력했는지 보여지게 함
- 메인화면을 css를 통해 배경화면 삽입 및 버튼들을 깔끔하게 함
- 짧은 글, 긴 글 사이트에 제시된 문장과 입력할 수 있는 칸을 정리함
- 짧은 글의 경우 1세트 (총 5번 입력)을 마치면 여태 입력한 문장들의 평균 정확도와 평균 타자율을 보여주도록 구현

-------

