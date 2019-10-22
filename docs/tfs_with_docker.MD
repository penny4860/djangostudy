# Tensorflow serving with docker

## 1. 준비물

* docker가 설치되어있는 host computer
* tensorflow docker image
	* tensorflow 에서 제공하는 docker image를 pull 받으면 된다.
* pre-trained 된 모델파일
	* saved_model 포맷

## 2. 실행방법

```
> docker run \
	--name serving \
	-p {grpc포트}:8500 \
	-p {rest_api포트}:8501 \
	-v {모델경로}:/model/{모델이름}
	-e MODEL_NAME={모델이름} \
	-t \
	tensorflow/serving:{텐서플로버젼}
```

* docker option
	* ```--name <serving>```
		* container에 이름을 설정
	* ```-p <호스트 포트>:<컨테이너 포트>```
		* 호스트에 연결된 컨테이너의 특정 포트를 외부에 노출
	* ```-v <호스트 디렉터리>:<컨테이너 디렉터리>```
		* 호스트와 공유할 디렉터리를 설정하여 파일을 컨테이너에 저장하지 않고 호스트에 바로 저장
	* ```-e MODEL_NAME=?```
		* 컨테이너에 환경 변수를 설정
	* ```-t```
		* Bash를 사용하기위한 옵션

