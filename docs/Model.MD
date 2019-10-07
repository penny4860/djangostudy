  
# Model
  
## 1. model

* 테이블을 정의하는 python class

## 2. model class 구현방법

* static 변수
	* Table column을 정의
* class method
	* Table 관련 동작을 정의하고 template에서 사용
	* 로직
		* view <-> model
		* view <-> template
			* template에서 모델 클래스에 정의해놓은 method를 사용
	* 사용예시
		* __str__(self)
			* 객체의 문자열 표현을 반환
		* get_absolute_url(self)
			* 해당 테이블의 url을 템플릿에서 사용
		* get_previous_post(self)
			* 해당 테이블의 이전 레코드의 url을 템플릿에서 사용
		* get_next_post(self)
			* 해당 테이블의 다음 레코드의 url을 템플릿에서 사용