FROM python:3.10-slim-buster

RUN apt update -y && apt install awscli -y


WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt
RUN pip install --upgrade accelerate
RUN pip uninstall -y transformer accelerate
RUN pip install transformer accelerate

CMD ["python3", "app.py"]