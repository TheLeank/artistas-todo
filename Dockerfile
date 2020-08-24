FROM python:rc-alpine3.12
RUN apk add --no-cache git
WORKDIR /var/app
RUN git clone https://github.com/TheLeank/artistas-todo-backend.git
WORKDIR /var/app/artistas-todo-backend
RUN python -m pip install -r requirements.txt
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0:8000"]