FROM python:3-onbuild
COPY . /usr/src/app

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
EXPOSE 8000
CMD ["python", "manage.py", "runserver" ,"0.0.0.0:8000"]