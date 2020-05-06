# M-Uwezo App

## Backend Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/BuildForSDG/team-159.git
$ cd team-159
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ python3 -m venv venv
$ source venv/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r backend/requirements/base.txt
```
Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd backend
(env)$ python manage.py createsuperuser
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/accounts/`.

