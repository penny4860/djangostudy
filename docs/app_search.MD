# Search 앱 구현

* 장고 9장
* search 로직
	* url -> view (get data from model) -> template

### 4. View

* SearchFormView 클래스
	* form_valid(form) 실행
		* return render(self.template_name, context)
	* context
		* template 파일에서 사용할수 있는 변수들을 묶어서 전달
		* context["form"]
		* context["search_term"]
		* context["object_list"]

### 5. Template

* template 실행 (post_search.html)
	* 하는 일
		* context로 전달받은 내용을 rendering
		* search form을 출력
		* user의 입력을 기다린다.
	* user가 키워드를 입력하면
		* 다시 똑같은 url을 실행하되, form의 전달내용이 update



