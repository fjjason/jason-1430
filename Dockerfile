FROM python:3.6.0
ENV PYTHONBUFFERED 1
ADD . /code
ADD requirements.txt /code/
WORKDIR /code
RUN pip install -r requirements.txt
CMD python app.py