# Wagtail_Boulangerie
Django Wagtail CMS Boulangerie
Wagtail is an open source CMS written in Python and built on the Django web framework.



## Install wagtail 
```shell
$ pip install wagtail 

``` 

## Generate your site

```shell
$ wagtail start boulangerie boulangerie
``` 

## Install project dependencies


```shell
$ cd boulangerie
$ pip install -r requirements.txt
$ pip install django_extensions

``` 
## Create the database

```shell
$ python manage.py migrate

``` 

## Create an admin user


```shell

$ python manage.py createsuperuser

```

## Start the server


```shell
$ python manage.py runserver

```
