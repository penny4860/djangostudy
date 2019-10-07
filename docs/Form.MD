  
# Form

## 1. HTML 에서의 form

* 웹 페이지에서의 입력 양식을 의미
	* <form> ~ </form> 사이에 있는 element 들의 집합
* 구성요소
	* input 태그
		* 실제로 사용자가 양식을 입력하기 위한 태그
	* form 태그 속성
		* action 속성
			* 폼 데이터가 전송되는 백엔드 url
		* method 속성
			* Get/ Post

```
<form method="post" action="/get/">
	<strong>아이디</strong>
	<input type="text" name="name" value="아이디 입력">
</form>
```

## 2. 장고의 폼 기능

* 장고의 폼처리기능
	1) 폼생성에 필요한 데이터를 폼 클래스로 구조화
	2) Form class에 있는 데이터를 rendering해서 HTML 폼 만들기
	3) user가 제출한 form/데이터를 수신/처리
* Form class
	* 폼 데이터를 기술
	* static 변수
		* template의 <input> element에 맵핑
* 장고에서 Form을 rendering
	* Unbound form : 데이터가 없는 form
	* bound form


## 3. Generic View에서의 폼처리

* FormView class에서 form 처리를 간단하게 구현할 수 있음
	* (static 변수) ```form_class``` 지정
	* (class method) ```form_valid(self, form)``` 구현

```
class MyFormView(FormView):
	form_class = MyForm
	template_name = ...
	success_url = ...
		
	def form_valid(self, form):
		return super(MyFormView, self).form_valid(form)
```

* template 에서는 view에서 전달한 form객체를 {{form}} 라는 이름으로 사용


