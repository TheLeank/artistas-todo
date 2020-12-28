# Backend for a to-do app

RESTful api made with Django for managing Tasks in a to-do list.

## Notice

This is a full Django project, as is aimed to test some functionalities. Do not use for production.

## Requirements

Docker and docker-compose.

## Setup

The project is ready to use. Clone it and execute `./manage.py migrate`.

## Requests

Get all tasks (GET):
http://localhost:8001/backend/tasks/

Get task (GET):
http://localhost:8001/backend/task/{id}/

Create task (POST):
http://localhost:8001/backend/task/
Params: text, body

Update task (PUT):
http://localhost:8001/backend/task/{id}/
Params: text, body

Delete task (DEL):
http://localhost:8001/backend/task/{id}/