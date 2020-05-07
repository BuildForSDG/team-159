FROM python:3.7
COPY . /usr/src/app

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
WORKDIR /usr/src/app
RUN pip install -r requirements/local.txt
EXPOSE 8000
CMD ["python", "manage.py", "runserver" ,"0.0.0.0:8000"]