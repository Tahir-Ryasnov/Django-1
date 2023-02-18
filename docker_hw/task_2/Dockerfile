FROM python:3.10.6

WORKDIR /proj

COPY ./proj /proj

RUN pip install -r /proj/requirements.txt

ENV SECRET_KEY oinioj9837782y3h87h87nm897nm879nm87y38789m,o8uo8990
ENV DEBUG True
ENV ALLOWED_HOSTS *

RUN python manage.py migrate

CMD ["gunicorn", "--bind", "0.0.0.0:8002", "stocks_products.wsgi"]
