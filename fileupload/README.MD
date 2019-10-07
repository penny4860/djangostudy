# FILE UPLOAD 앱

* 질문
	* template 파일을 앱별로 나누자
	* 업로드한 텍스트 파일을 저장하고 읽는 방식이 아니라, 메모리에서 바로 읽을 수 없을까?
		* [views.py](views.py) 에서 handle_uploaded_file()
* 참고자료
	* https://docs.djangoproject.com/en/2.2/topics/http/file-uploads/#basic-file-uploads

## 1. 로직

## 2. 구현과정

### 1) skeleton 만들기

### 2) model 코딩

### 3) URLConf 구현

[urls.py](urls.py)

```
# project/urls.py
urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload/', views.upload_file, name='upload'),
]
```

### 4) view 구현

[views.py](views.py)

* 뷰 함수 : ```def upload_file(request):```
	* ```return render(request, 'upload.html', {'form': form, "contents": contents})```
	* template 파일에 context를 dict 형으로 전달
    	* template 에서는 ```{{form}}```, ```{{contents}}```으로 사용

### 5. template 구현

[upload.html](../templates/upload.html)

