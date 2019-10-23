# CSS3

[CSS: 선택자(Selector) 이해](http://www.nextree.co.kr/p8468/)

* HTML : 웹 콘텐츠에 의미를 부여하고 구조를 형성
* CSS : 시각적인 디자인과 레이아웃 표현
	* 반응형 웹 : 다양한 디바이스에 대응하는 웹

## 1. CSS를 적용하는 방법

1. inline
	* 태그에 style 속성을 추가하고 css 코드를 작성
2. embedded
	* head 태그안에서 작성
3. external
	* 별도의 css 파일을 작성하고 html에서 이를 가져온다.

## 2. Selector (선택자)

css style을 적용할 element를 선택하는 방법

### 2.1. 태그 선택자

```	
/* CSS */
p { background: yellowgreen; color: darkgreen; }

<!-- HTML -->  
<p>태그 선택자(Type Selector)</p>  
<div>태그 선택자(Type Selector)</div>  
```

### 2.2. 클래스 선택자

```
/* CSS */
.class1 { background: yellowgreen; color: darkgreen; }
div.class2 { background: darkgreen; color: yellowgreen; }

<!-- HTML -->  
<p class="class1">클래스 선택자(Class Selector)</p>  
<p class="class2">클래스 선택자(Class Selector)</p>  
<div class="class2">클래스 선택자(Class Selector)</div>  
```


### 2.3. 아이디 선택자


```
/* CSS */
#id1 { background: yellowgreen; color: darkgreen; }
div#id2 { background: darkgreen; color: yellowgreen; }

<!-- HTML -->  
<p id="id1">ID 선택자(ID Selector)</p>  
<p id="id2">ID 선택자(ID Selector)</p>  
<div id="id2">ID 선택자(ID Selector)</div>  
```




