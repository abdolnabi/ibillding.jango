<p align="center">
    <img src="https://img.shields.io/badge/Version-0.5.0--alpha.178-brightgreen.svg" alt="Version">
</p>

# iBillding

## Table of contents

* [iBillding](#ibillding)
  + [Table of contents](#table-of-contents)
  + [Intro](#intro)
  + [Development](#development)
  + [Contributors](#contributors)
  + [Testing](#testing)
  + [Deployment](#deployment)
    - [Staging](#staging)

## Intro

iBillding is a Building Charge Management system.

## Development

* Using Django stack.

## Contributors

* [Nabi Zameni](https://github.com/abdolnabi), CEO & CTO
* [Reza Amiri](https://github.com/reza-renewablion), Backend Developer
* [Fateme Salehnia](https://github.com/fsalehnia), Frontend Developer
* [Hosein Hashemi](#), UI/UX Designer
* [Mohsen Sadeghzade](https://github.com/TechieForFun), Software Engineer

## Testing

* No tests so far

## Deployment

### Staging

0. Clone the repo

1. Install Gunicorn, MySQL 5.7+, NPM

2. Create a `user` with `secret` as password in MySQL. Then create a DB like `billding` .

``` sql
MySQL> CREATE USER 'user'@'localhost' IDENTIFIED BY 'secret';
mysql> CREATE DATABASE `billding` ;
MySQL> GRANT ALL PRIVILEGES ON billding.* to user@localhost
MYSQL> ALTER USER 'user'@'localhost' IDENTIFIED BY 'secret';
```

3. Copy `.env.example` to `.env` and set variables.

4. Run

``` console
root@terminal$ apt install gunicorn3
root@terminal$ apt install libpq-dev
root@terminal$ apt install default-libmysqlclient-dev
root@terminal$ apt install python3-pip
root@terminal$ pip3 install django-admin
root@terminal$ pip3 install -r requirements.txt
root@terminal$ python3 bcm/manage.py migrate --noinput
root@terminal$ npm install
root@terminal$ python3 bcm/manage.py collectstatic --noinput
root@terminal$ cp -rf node_modules staticfiles
```

5. Then run the application with:

``` console
root@terminal$ gunicorn3 bcm.wsgi:application --chdir bcm --bind 0.0.0.0:80 --workers=1
```
