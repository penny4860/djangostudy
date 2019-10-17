
# Django Restframework Tutorial

## 질문

### 1. Solved

* http method 중 PUT / POST의 차이점
	* POST : client 에서 리소스의 위치를 명시
	* PUT : client 에서 리소스의 위치를 지정하지 않음.
* rest API로 구현했을때 web browser로 테이블에 데이터 추가는 못하나? (view함수의 request.POST로 타는 방법)
	* command line에서 httpie 설치하고 http 명령어를 쓸수 있음.
	* 예시) : ```http --form POST http://127.0.0.1:8000/snippets/ code="print(123)"```
* django api에서 client server간 데이터 통신 방법
	* 클라이언트 command
		* ```http --form POST http://127.0.0.1:8000/imgsize/ file="tmp.jpg"```
	* 장고서버
		* django view 함수에서 request.POST["file"]로 클라이언트에서 전송한 데이터를 받을 수 있음.

### 2. Working on

* api_view() 를 사용한 뷰함수 구현시, image file upload를 브라우져에서 하는 방법
* api_root는 왜 만드는거지?
* urls.py에서 router를 사용하는 이유? 장점?
	* 뷰셋을 사용하지 않으면 router를 사용하지 않아도 되는건가?
	* HTTP method, action에 대해서 다양한 동작을 정의할 수 있는듯.
		* 맞는지 모르겠음.

## restful API 구현방법

1) django 만을 사용
	* 뷰함수에서 JsonResponse 객체를 리턴
2) django restframework : serializer 사용
	* Serialize 클래스 구현
		* ```ResponseInfo```
		* ```ResponseSerializer```
	* 뷰함수 구현
		1) ```ResponseInfo``` 객체를 생성
		2) ```ResponseSerializer``` 객체로 wrapping
			* ```serializer = ResponseSerializer(response_info)```
		3) JsonResponse 객체를 리턴
			* ```return JsonResponse(serializer.data)``` 
3) django restframework : api_view() 데코레이터 사용
	* 장점 
		* browserble API를 사용할 수 있다. : 브라우저에서 http get/post를 조절해서 테스트할 수 있음.
			* ```django-project> http --form POST http://127.0.0.1:8000/imgsize/ file="1.png"```
			* web-browser에서 content에 ```{"file" : "1.png"}```를 입력
	* 수정사항
		1) api_view 데코레이터로 뷰함수를 감싼다.
			* ```@api_view(['GET', 'POST'])```
		2) 함수입력
			* HttpRequest 객체 -> Request 객체
		3) 함수출력
			* JsonResponse 객체 -> Response 객체

## restful API 구현과정

### 2. model 코딩

#### 2.1 model

#### 2.2 serializer 구현 

1) Serializer class를 상속 : ```class SnippetSerializer(serializers.Serializer):```
2) fields 데이터를 static 변수로 정의
3) ```create(self, validated_data):```
4) ```update(self, instance, validated_data):```

### 4. view 구현

* 웹 앱과 restful API의 차이
	* 웹 앱
		* HttpResponse 객체를 리턴 (template을 포함)
	* restful API
		* JsonResponse 객체를 리턴 (template은 구현할 필요 없음)

* restful API의 뷰함수 구현방법
	* django 기능만 사용
		* 뷰함수에서 JsonResponse() 객체를 리턴하도록 구현
			1) @csrf_exempt 데코레이터
			2) 함수 input : Request objects
			3) request.method에 따라 분기
			4) 함수 output : JsonResponse() 객체
				* serializer.data를 포함
	* django restframework : api_view 데코레이터 사용
		1) ```@api_view``` 데코레이터 사용
		2) HttpRequest -> Request 객체가 입력
		3) JsonResponse -> Response 객체를 리턴
		4) Response 객체의 status를 interger 대신 status 모듈에 정의되어있는 코드를 사용


```
# django web application의 뷰
# HttpResponse 객체를 리턴
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

# django rest API의 뷰
# JsonResponse 객체를 리턴
@csrf_exempt
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
```

