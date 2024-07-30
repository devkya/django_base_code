cd server

python manage.py makemigrations
python manage.py migrate
uvicorn server.asgi:application --host 0.0.0.0 --port 8001 --reload
