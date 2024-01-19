# Django Base Code
## 00. 필수 패키지 설치 및 프로젝트 생성
1. `pipenv install django django-environ djangorestframework psycopg2-binary django-cleanup channels channels-redis django-cors-headers djangorestframework-simplejwt drf-spectacular gunicorn daphne boto3 django-storages `
2. `django-admin startproject server`

## 01. 환경 설정
### `settings.py` 분리
1. 개발, 프러덕션 환경을 분리하기 위해 `settings.py`를 `base.py`, `development.py`, `production.py`로 분리한다. `BASE_DIR`에 유의하자!

2. 베이스 코드에서는 `SECRET_KEY`를 랜덤 생성한다. 생성 후 base.env에 고정값으로 등록해야 함(프로젝트 리빌드 시 JWT `SIGNING KEY`가 변경되면서 `token`이 유효하지 않는 문제 발생)

3. `third party` 라이브러리 설정
  * [rest_framework](https://www.django-rest-framework.org/)