# Image Display 앱 : 모델에 있는 image 를 template 에서 렌더링하는 예제 앱

### 1. skeleton 만들기

### 2. 모델 코딩

* ImageField 를 static 변수로 갖고있는 모델 클래스 구현

```
class Post(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')


    def __str__(self):
        return self.title
```

### 3. URL

### 4. View

```
class HomePageView(ListView):
    model = Post
    template_name = 'posthome.html'
```

* 구현
	* ListView 로 view 클래스 구현
* 로직
	* Post 모델(테이블)을 가져온다.
	* 모델을 ```{{object_list}}```로 template 에 넘긴다.


### 5. Template

```
<ul>
  {% for post in object_list %}
    <h2>{{ post.title }}</h2>
    <img src="{{ post.cover.url}}" alt="{{ post.title }}">
  {% endfor %}
</ul>
```

* 구현
	* 뷰에서 받은 전체 테이블은 ```{{object_list}}``` 로 사용
		* for문을 돌면서 1개 field를 꺼낸다.
			* {{ post.cover.url}} 로 image source를 지정

