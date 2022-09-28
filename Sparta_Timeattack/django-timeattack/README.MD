# 9/26 쪽지시험
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

python manage.py runserver

# 9/27 쪽지시험
### . models.py에 AccessLog 테이블을 생성해주세요

- 필드
    - created_at : 데이터가 생성된 시간을 알 수 있도록 datetimefield 사용
    - location : 사용자가 어떤 template에 접근했는지 알 수 있도록 charfield 사용

### 2. 생성된 테이블을 makemigrations / migrate 명령어를 통해 db에 반영해주세요

### 3. 생성한 테이블을 admin.py에 등록해주세요

### 4. 사용자가 introduce 페이지에 접속했을 때, 접속 로그를 남겨주세요

- admin 페이지에서 로그를 봤을 때 언제 어떤 페이지에 접속했는지 알 수 있어야 합니다.
- 로그를 저장할 때는 어떤 탬플릿을 조회했는지도 확인할 수 있도록 해주세요

### 5. admin 페이지에 접속해서 접속 기록을 확인해주세요

# 9/28쪽지시험
## 오늘의 목표 - User Model 확장하기

1. 프로젝트에 사용될 폴더를 생성하고, 편집기에서 생성한 폴더를 열어주세요.
2. 파이썬 가상 환경을 생성하고 활성화해주세요.
3. Django 패키지를 설치해주세요.
4. spartatest라는 django 프로젝트를 생성해주세요
5. customuser라는 앱을 생성해주세요
6. settings.py에 앱을 등록해주세요.
7. Django의 User를 기반으로 만든 CustomModel라는 클래스를 만들어주세요.
- 조건: 테이블 이름은 custom_user
- Django의 User 모델에서 아래의 필드를 추가해주세요.
    - address (TextField, max_length=500, blank=True)
    - bio (TextField, max_length=500, blank=True)
    
    힌트: class CustomModel(AbstractUser)
    
1. Django에게 기본 인증과정 (AUTH_USER_MODEL)을 customuser 앱에 작성한 CustomModel로 사용하겠다! 라고 알려주세요.
    
    힌트: [settings.py](http://settings.py/)
    
2. 데이터베이스에 변경사항을 반영하고 적용해주세요.
3. 관리자 계정을 만들어주세요.
4. Admin 사이트에서 CustomModel를 볼 수 있도록 적용해주세요.
    
    서버를 켜고 CustomModels에서 아래와 같이 address와 bio를 볼 수 있다면 성공입니다.
