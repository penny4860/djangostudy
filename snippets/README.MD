
# Django Restframework Tutorial

## 질문

* rest API로 구현했을때 web browser로 테이블에 데이터 추가는 못하나? (view함수의 request.POST로 타는 방법)
* model serializer 말고 일반 serializer 사용법?


## 구현과정

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
	1) @csrf_exempt 데코레이터
	2) 함수 input : request
	3) request.method에 따라 분기
	4) 함수 output : JsonResponse() 객체
		* serializer.data를 포함

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

