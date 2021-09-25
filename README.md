Cornershop Backend Challenge Test
==============

This is a Docker (with docker-compose) environment for Cornershop Backend Test development.

[![Build Status](https://github.com/nietzscheson/cornershop-backend-test/workflows/Build/badge.svg)](https://github.com/nietzscheson/cornershop-backend-test/actions)

# Installation

1. First, clone this repository:

```bash
$ git clone https://github.com/nietzscheson/cornershop-backend-test
```

2. Copy the environment vars:

```bash
$ cp .env.dist .env
```
3. Configure SLACK_API_TOKEN in .env:

```bash
$ SLACK_API_TOKEN=<PUT_SLACK_TOKEN_HERE>
```
4. Init project
```bash
$ make
```
***The before make command start all necesary containers to run the application.***

6. Show containers:
```bash
$ make ps
```
This results in the following running containers:

```bash
> $ docker-compose ps
                 Name                               Command               State                                          Ports
---------------------------------------------------------------------------------------------------------------------------------------------------------------------
celery                                   celery -A core worker -l i ...   Up
core                                     /bin/sh -c python manage.p ...   Up       0.0.0.0:8000->8000/tcp,:::8000->8000/tcp
cornershop-backend-test_default-core_1   python3                          Exit 0
cornershop-backend-test_selenium_1       /opt/bin/entry_point.sh          Up       0.0.0.0:4444->4444/tcp,:::4444->4444/tcp, 0.0.0.0:5900->5900/tcp,:::5900->5900/tcp
postgres                                 docker-entrypoint.sh postgres    Up       0.0.0.0:5432->5432/tcp,:::5432->5432/tcp
redis                                    docker-entrypoint.sh redis ...   Up       0.0.0.0:6379->6379/tcp,:::6379->6379/tcp
```
*The POS Application can be accessed from: [localhost:8000](http://localhost:8000)*
___

If you want to test the application manually, please load the fixtures data:
```bash
$ make loaddata
```
**`Users fixtures`** for access to the. Passwords in plain text:
| username | password       | is_superuser |
| -------- | ---------------| -------------|
| ana      | `password1234` | True         |
| miguel   | `password123!` | False        |
___
If you love the automation testing, please run:
```bash
$ make test
```
This project is configured with a Selenium node. If you want to look how interact with a browser please use your prefer viewer. We recomended [VCN](https://www.realvnc.com/es/connect/download/viewer/) and connect with localhost:5900 | password
___