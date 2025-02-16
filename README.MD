
## Note

* 질문
	* Generic View (FormView) 에서 class method인 form_valid(form)로 template에 데이터를 넘길 때, template에서 이 데이터를 받는 변수이름?
		* {{form}} // {{object}} ?

* 해결된 질문
	* form class의 역할? (solved)
		* template에 전달할 form data를 기술	
	* urls.py에서 사용하는 urlpattern 이름(path 함수의 name 파라메터)의 용도는?
		* 프로젝트 템플릿파일에서 사용
	* API endpoint?
		* [rest](docs/rest.MD)
		
* Todo


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

* urlconf 구현하는 방법
	1) 프로젝트/urls.py
 		* django app의 대표주소와 namespace를 지정
		* ```path('imgsize/', include("imgsize.urls", namespace="imgsize")),```
	2) 앱/urls.py
		* ```app_name```을 지정
			* 프로젝트/urls.py 에서 지정한 앱의 namespace와 같아야함.
		* 앱내부의 상대주소와 뷰를 맵핑하고, name을 지정
			* ```path('index/', views.requested_url ,name="index"),```

* include() 에서 namespace를 지정하는 이유?
	* index.html 과 같은 프로젝트의 template 에서 사용
		* ```<a href="{% url 'imgsize:index' %}">```

### 4. view 구현

* views.py : 로직 작성
* generic view 구현방법
	* [View](docs/View.MD)


### 5. template 구현

* app/templates 디렉토리
* template 구현방법
	* [Template](docs/Template.MD)
	* [Index page 구현 방법](docs/IndexTemplate.MD)


