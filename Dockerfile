FROM python:3.8.7

WORKDIR /code

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .


CMD ["python", "./etl_run.py"]


