from django.shortcuts import render

# Create your views here.

def mainpage(request):
    context = {
        'generation': 13,
        'info': {'weather': '한강가기 좋은 날씨', 'feeling': '코딩 재밌다~', 'note': '아기사자화이팅!'},
        'shortKeys': [
            'Templates: 유저에게 제공할 파일의 구조나 레이아웃을 관리하기 위해 사용함 (ex.HTML,CSS)',
            'views.py작성->urls.py작성->html페이지와 view연결',
            'templates 언어: view에 작성된 data 가져오기, 반복문 등의 기능을 수행함',
            '템플릿 변수: {{ 변수명 }}, 템플릿 태그: if문, for문',
            'template 상속: base.html 파일생성->block 지정->mainpage와 secondpage 업데이트',
            'nav bar 분리(코드 반복 줄이기): _navbar.html 파일생성->nav영역 옮기기->base.html에 상속',
            'static: 정적인 파일을 저장하는 디렉토리 (ex.CSS & image)'
        ]
    }
    return render(request, 'main/mainpage.html', context)

def secondpage(request):
    return render(request, 'main/secondpage.html')