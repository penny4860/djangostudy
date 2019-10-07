  
# View

* 질문
	* form view에서 재정의하는 method ```def form_valid(self, form):```에서 form은 무엇인가?
		* argument form은 client쪽에서 전송한 정보가 form_class type의  객체로 들어온다.
	
* Reference: 장고책 15장 (장고핵심기능 : View)
  
## 1. Generic View 의 종류

### Template View

1) 설명 : 화면에 보여줄 template 을 연결
2) 재정의
	* template_name
3) 예제 : 

```
class HomeView(TemplateView): template_name = "home.html"
```

### RedirectView

1) 설명 : 주어진 url로 redirect
2) 재정의
	* url
3) 예제 : 
	* ```class HomeView(RedirectView): url = "/blog/post/"```

### DetailView

1) 설명 : 특정객체 1개의 정보를 display
2) 재정의
	* model
	* template_name
3) 예제 : 
	* ```class HomeView(DetailView): model = Post```
	* template file에서 ```{object}``` 로 사용

### ListView

* template file에서 ```{object_list}``` 로 사용


### FormView

1) 설명 :
2) 재정의
	* form_class
	* template_name
	* success_url
	* form_valid(form)
3) 예제 : class SearchFormView(FormView): model = Post
	* template file에서 {object} 로 사용


## 2. Generic View 오버라이딩

### 2.1 속성

* model (query_set)
	* 뷰가 출력할 데이터가 있는 모델 클래스
* template_name
	* template file 이름
* form_class
	* form을 만드는데 사용하는 클래스
* success_url
	* form에 대한 처리가 성공한 이후에 리다이렉트될 URL을 지정
* context_object_name
	* template에서 사용할 context 변수이름

### 2.2 method

* get_query_set()
	* 출력 대상인 객체리스트를 반환
* get_context_data()
	* template에서 사용할 context 를 반환
* form_valid(form)
	* success_url로 리다이렉트를 수행


