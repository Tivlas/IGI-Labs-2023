FROM python:alpine

WORKDIR /lab2_task2

RUN mkdir ./users_data

VOLUME ./users_data

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./src .

CMD ["python","main.py"]