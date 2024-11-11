FROM python:3.9-slim

WORKDIR /app_python

COPY requirements.txt ./
COPY ./app_python/ .

EXPOSE 8000 8000

RUN adduser --disabled-password foo && chmod 777 /app_python/visits.txt

RUN pip install --no-cache-dir -r requirements.txt

USER foo

CMD ["python", "app_python.py", "runserver", "--host", "0.0.0.0", "--port", "8000"]