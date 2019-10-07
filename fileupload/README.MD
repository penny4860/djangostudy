# FILE UPLOAD 앱

* 질문


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

### 5. template 구현

[upload.html](../templates/upload.html)

