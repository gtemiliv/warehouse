FROM python:3.12

WORKDIR /app

COPY ./warehouse .
RUN pip install -r requirements.txt

EXPOSE 80:5000

CMD ["flask", "--app", "app", "run", "-h", "0.0.0.0"]