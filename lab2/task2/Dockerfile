FROM python

WORKDIR /lab2_task2

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./src .

CMD ["python","main.py"]