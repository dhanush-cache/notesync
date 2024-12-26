FROM python:3.12.8-alpine3.21
RUN apk add --no-cache gcc musl-dev mariadb-dev
RUN pip install pipenv
RUN addgroup notesyncadmin && adduser -S -G notesyncadmin notesyncadmin
USER notesyncadmin
WORKDIR /notesync
COPY Pipfile .
RUN pipenv install --dev
COPY . .
EXPOSE 8000
CMD [ "pipenv", "run", "python", "manage.py", "runserver", "0.0.0.0:8000" ]
