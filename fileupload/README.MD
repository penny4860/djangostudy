# FILE UPLOAD 앱

* 질문
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

