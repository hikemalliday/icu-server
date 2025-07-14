FROM python:3.10-alpine
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
COPY .env /app/.env
#CMD ["python", "manage.py", "start_bot"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]