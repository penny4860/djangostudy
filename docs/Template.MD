
# Template System

* template 파일
	* html 포맷
	* (html code + template code) 로 구성
	* (html code + template code) ====> html code file
		* 장고의 template 시스템이 html file로 변환시켜서 client에 rendering


## 1. template 변수

## 2. template filter

## 3. template 태그

* "% url %" 태그
	* 소스코드에 url 주소를 하드코딩하지 않게 해줌
	* "{% url 'namespace:view-name' arg1 arg2 .. %}"
		* namespace
			* app_name 변수
		* view-name
			* urls.py에서 path함수의 name 인자로 정의한 pattern이름
		* argN
			* view 함수에서 사용하는 인자