### 1. 프로젝트에 사용될 폴더를 생성하고, 편집기에서 생성한 폴더를 열어주세요

mkdir django-project

cd django-project

### 2. 파이썬 가상 환경을 생성하고 활성화 해주세요

python -m venv venv

source ./venv/bin/activate

### 3. django 패키지를 설치해주세요

pip install django

### 4. spartatest라는 django 프로젝트를 생성해주세요

django-admin startproject spartatest

cd spartatest

### 5. introduce라는 앱을 생성해주세요

python manage.py startapp introduce

### 6. introduce/templates 경로에 간단한 자기소개를 적은 탬플릿 html을 만들어주세요

1. project의 settings.py에서 installed app에 introduce 적기
2. project의 urls..py에서 include import 하고 path(’’, include(’introduce.urls’)) 경로 적기
3. app의 urls.pyurls.py를 만들고 path, views import 하고 path(’introduce/’,views.index) 경로 적기
4. app의 views.py에서 def index(request) return render(request, ‘introduce/index.html’) 함수 적기
5. templates 폴더를 만든 다음 샌드위치 구조로 introduce폴더도 만들고 index.html 파일 만들기
6. index.html 자기소개 적기

### 7. 127.0.0.1:8000/introduce/ 경로의 페이지에 접속했을 때 자기소개 페이지가 보일 수 있도록 설정해주세요

python manage.pymanage.py runserver