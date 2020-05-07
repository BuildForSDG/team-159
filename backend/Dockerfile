FROM python:3.7
COPY . /usr/src/app

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
RUN pip install -r requirements/production.txt
EXPOSE 8000
CMD ["python", "manage.py", "runserver" ,"0.0.0.0:8000"]