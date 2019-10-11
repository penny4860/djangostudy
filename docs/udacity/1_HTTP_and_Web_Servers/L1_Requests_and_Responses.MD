# L1 : Requests and Responses


## Note

* Http : client와 서버의 통신방법
* web server
	* 네트워크상의 다른 프로그램(client)으로부터의 connection을 accept하는 프로그램
* URI
	* URI : 네트워크상에서 리소스의 고유위치
	* 구성 : ```https://en.wikipedia.org:443/wiki/Fish```
		* scheme : ```http/file/https```
			* resource에 대한 접근방법을 정의
				* file : 호스트의 local file에 접근
				* http : 호스트의 웹서버에 접근
		* hostname : ```en.wikipedia.org```
			* host is a computer on the network
			* IP 주소
		* port number ```:443```
			* host computer에서 서로다른 process를 구분
			* scheme에 따른 디폴트 port number가 존재하기때문에 일반적으로는 생략한다.
				* http : 80
				* https : 443
		* path : ```/wiki/Fish```
			* host 내부경로
* HTTP request message
	* "GET /readme.png HTTP/1.1"
		1) HTTP method
		2) path of the resource
		3) protocol
* HTTP response message
	1) status line : 
		* 예시
			"HTTP/1.1 301 Moved Permanently"
			"HTTP/1.0 200 OK"
		* The status line tells the client whether the server understood the request, whether the server has the resource the client asked for, and how to proceed next.
	2) header
	3) response body


