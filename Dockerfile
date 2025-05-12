
FROM python:3.8.5-slim-buster

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt
RUN pip install scikit-learn==1.6.1
CMD ["python3", "app.py"]

