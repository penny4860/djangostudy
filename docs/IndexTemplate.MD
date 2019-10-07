# 프로젝트 index page 구현하기  

템플릿 코딩과정이 주가됨

* base.html에서 프로젝트 전체의 template 구조를 구현
	* header / menu는 모든 페이지에서 공통
	* content / footer는 각 페이지마다 다르게 구현
* 다른 html
	* base.html 을 상속
	* content / footer를 구현
* 링크주소를 설정하는 방법
	* ```<li><a href="#">Home</a></li>```
		* 해당 page의 윗부분으로 이동
	* ```<li><a href="% url 'home' %">Home</a></li>```
		* urls.py에서 정의했던 home이름의 url로 이동하는 링크


## 1. base.html 페이지 구현

* header
* body
	* header 영역
		* ```<div id="header"> ... </div>```
	* menu 영역
		* ```<div id="menu"> ... </div>```
	* content 영역
		* ```<div id="content"> {% block content %}{% endblock %} </div>```
			* 실제 내용을 하위 template 에서 결정
	* footer 영역
		* ```<div id="footer"> {% block footer %}{% endblock %} </div>```
			* 실제 내용을 하위 template 에서 결정

## 2. base.css 구현

* html 파일에서 div 태그로 지정한 영역의 스타일을 정의

## 3. home.html

* ```{% extends "base.html" %}```
	* base.html 페이지 코드를 상속
* ```{% block content %}{% endblock %}```
	* base.html 페이지 내용을 재정의





