FROM python:rc-alpine3.12
WORKDIR /var/app
RUN apk add git
RUN python -m pip install Django
RUN django-admin startproject artistas_todo
WORKDIR /var/app/artistas_todo
RUN ["python", "manage.py", "startapp", "backend"]
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0:8000"]