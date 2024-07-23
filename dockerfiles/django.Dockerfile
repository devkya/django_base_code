FROM python:3.11.2-slim

# 환경 변수 설정
# 즉시 출력
ENV PYTHONUNBUFFERED=1
# .pyc (Python 컴파일된 바이트 코드) 파일을 생성하지 않도록 하는 역할
ENV PYTHONDONTWRITEBYTECODE=1

# 패키지 설치
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    python3-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# requirements.txt를 먼저 복사하여 캐시 활용
COPY requirements.txt .

RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt \
    && rm -rf /root/.cache/pip

# 애플리케이션 소스 코드 복사
COPY server /app/server
COPY scripts/django-run.sh /app/
RUN chmod +x /app/django-run.sh

# ENTRYPOINT로 스크립트 실행
ENTRYPOINT ["sh", "-c", "/app/django-run.sh"]

