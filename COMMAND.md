# 개발 서버 실행 방법

### 파이썬
1. 현재 버젼은 3.11.2로 되어있음

### 가상환경 설치 & 실행
1. `pipenv install`
2. `pipenv shell` 

### docker 실행
1. `docker-compose -f docker-compose-dev.yml up --build` : 로그를 볼 수 있게 실행
2. `docker-compose -f docker-compose-dev.yml up --build -d` : 백그라운드 실행