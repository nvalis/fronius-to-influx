FROM python:3

WORKDIR /usr/src/app

ADD requirements.txt .
RUN python -m pip install -r requirements.txt
ADD src .

CMD python main.py

