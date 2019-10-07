# Image Upload 앱 : user가 업로드한 이미지를 모델에 반영

### 2. 모델 코딩

Image Display 앱 참조

### 3. URL

### 4. View

```
class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post.html'    
    success_url = reverse_lazy('home')
```

```
class PostForm(forms.ModelForm):


    class Meta:
        model = Post
        fields = ['title', 'cover']
```


* 구현
	* CreateView 로 view 클래스 구현
        * model, form_class, success_url지정
    * ModelForm으로 form 클래스 구현
* 로직
	* 폼을 가져와서 template에 넘긴다.
	* 템플릿에서는 ```{{form}}```으로 사용


### 5. Template


```
<form method="post" enctype="multipart/form-data">
  {% csrf_token %}
  title : {{ form.title }}
  image cover : {{ form.cover }}
  <button type="submit">Submit New Post</button>
</form>
```

* 구현
	* 뷰에서 받은 폼양식을 ```{{form}}``` 로 사용