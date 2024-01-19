# Django Base Code
## 00. 필수 패키지 설치 및 프로젝트 생성
1. `pipenv install django django-environ djangorestframework psycopg2-binary django-cleanup channels channels-redis django-cors-headers djangorestframework-simplejwt drf-spectacular gunicorn daphne boto3 django-storages `
2. `django-admin startproject server`

## 01. 환경 설정
### `settings.py` 분리
1. 개발, 프러덕션 환경을 분리하기 위해 `settings.py`를 `base.py`, `development.py`, `production.py`로 분리한다. `BASE_DIR`에 유의하자!

2. 베이스 코드에서는 `SECRET_KEY`를 랜덤 생성한다. 생성 후 base.env에 고정값으로 등록해야 함(프로젝트 리빌드 시 JWT `SIGNING KEY`가 변경되면서 `token`이 유효하지 않는 문제 발생)

3. `third party` 라이브러리 설정
  * [drf](https://www.django-rest-framework.org/)
  * [django-cors-headers](https://pypi.org/project/django-cors-headers/) : `CORS`, `CSRF` 추가
  * [drf-spectacular](https://drf-spectacular.readthedocs.io/en/latest/)
  * [drf-simplejwt](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)
  * [django-cleanup](https://pypi.org/project/django-cleanup/) : `ImageField`, `FileField` 인스턴스 삭제 시 파일 삭제해주는 라이브러리

4. STATIC & MEDIA & TEMLATES
  * `static` 폴더가 앱 내에 있는 경우 `STATICFILE_DIRS` 설정해야 함

5. `env` 설정
  * `BASE_DIR`에 env 폴더를 생성하고 `base.env`, `development.env`, `production.env`를 생성함

6. `logging` 설정[링크](https://kincoding.com/entry/Google-Gmail-SMTP-%EC%82%AC%EC%9A%A9%EC%9D%84-%EC%9C%84%ED%95%9C-%EC%84%B8%ED%8C%85)
  * `base.env` `LOGGING_NAME, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, EMAIL_SUBJECT_PREFIX, EMAIL_LIST` 변경 필요


## 02. Docker 설정
1. `docker-compose.yml` 포트 및 이름 변경
2. `env/dev.env, env/prod.env` 환경 변수 설정
3. `nginx.conf` 도메인 이름 변경


## 03. Github Action(CI/CD)
1. `deploy.yml` 수정사항
  * github settings 에서 `HOST`, `USERNAME`, `SSH_KEY` 설정해야 함
  * script 에서 ec2 디렉토리 수정해야 함



