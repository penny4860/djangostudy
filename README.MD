
## Note

* 질문
	* urls.py에서 사용하는 urlpattern 이름(path 함수의 name 파라메터)의 용도는?
	* Generic View (FormView) 에서 class method인 form_valid(form)로 template에 데이터를 넘길 때, template에서 이 데이터를 받는 변수이름?
		* {{form}} // {{object}} ?
	* form class의 역할? (solved)
		* template에 전달할 form data를 기술	
	* API endpoint? (solved)
		* [rest](docs/rest.MD)
		
* Todo
	* django rest framework + keras를 이용한 웹 API 구현소스코드 리뷰
		* https://medium.com/@att288/deploy-multiple-keras-models-in-django-project-e3b34ed23cbb

## 장고 구현과정

### 1. skeleton 만들기

1) 프로젝트 생성 : startproject
2) 프로젝트 설정파일 수정 : settings.py
    * DATABASES
    * TEMPLATES
        * TEMPLATES['DIRS'] 에 프로젝트 template file위치를 지정
    * static files
        * STATICFILES_DIRS 에 프로젝트 static file위치를 지정
    * TIME_ZONE
    * media 관련내용
        * MEDIA_ROOT
    * INSTALLED_APPS
        * 사용할 앱을 등록
3) 기본 테이블 생성
    * python manage.py migrate
4) 관리자생성
    * python manage.py createsuperuser
5) 앱생성
    * python manage.py startapp bookmark
6) 앱등록 : settings.py


### 2. model 코딩

* models.py : 사용할 테이블에 따라 model class 구현
* admin.py : 구현한 model class 를 admin site에 등록
* makemigrations : DB에 반영
* migrate : 테이블 생성
* model 구현방법
	* [Model](docs/Model.MD)

### 3. URLConf 구현

* urls.py : URL 정의


### 4. view 구현

* views.py : 로직 작성
* generic view 구현방법
	* [View](docs/View.MD)


### 5. template 구현

* app/templates 디렉토리
* template 구현방법
	* [Template](docs/Template.MD)
	* [Index page 구현 방법](docs/IndexTemplate.MD)


