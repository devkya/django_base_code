FROM python:3.11.2-slim

# 환경 변수 설정
# 즉시 출력
ENV PYTHONUNBUFFERED=1
# .pyc (Python 컴파일된 바이트 코드) 파일을 생성하지 않도록 하는 역할
ENV PYTHONDONTWRITEBYTECODE=1

# 패키지 설치
RUN apt-get update && apt-get install -y libpq-dev \
    gcc \
    python3-dev \
    && apt-get clean


WORKDIR /app

# 애플리케이션 소스 코드 복사
COPY . .

RUN pip3 install --upgrade pip
RUN pip3 install pipenv

RUN pipenv requirements > requirements.txt
RUN pip3 install -r requirements.txt

# 스크립트 파일 복사하고 실행 권한 부여
RUN chmod +x scripts/django-run.sh

# ENTRYPOINT로 스크립트 실행
ENTRYPOINT ["sh", "-c", "scripts/django-run.sh"]
