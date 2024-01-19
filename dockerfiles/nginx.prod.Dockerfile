# nginx 최신 버전 사용
FROM nginx:latest

# nginx 설정 파일 복사
COPY ./nginx/nginx.conf /etc/nginx/nginx.conf

# 정적 파일 복사
COPY ./server/staticfiles /staticfiles

# 기타 필요한 설정 추가 (예: SSL 설정 등)
