## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
This project is made for one of the Lodz University courses.
	
## Technologies
Project is created with:
* Python
* Django
	
## Setup
### Installing locally
```
$ python -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py collectstatic
$ python manage.py runserver 0.0.0.0:8000
```
### Using Docker
#### Building manually
```
$ docker build -t meme_site:latest .
$ docker run -d -p 8000:8000 meme_site:latest
```
#### Downloading already built project
```
$ docker pull ziomkangur/jwp2:latest
$ docker run -d -p 8000:8000 ziomkangur/jwp2:latest 
```
