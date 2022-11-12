Cornershop Backend Challenge Test
==============

This is a Docker (with docker-compose) environment for Cornerpos development.

[![Build Status](https://github.com/nietzscheson/cornerpos/workflows/Build/badge.svg)](https://github.com/nietzscheson/cornerpos/actions)

# Installation

1. First, clone this repository:

```bash
$ git clone https://github.com/nietzscheson/cornerpos
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
NAME                       COMMAND                  SERVICE             STATUS              PORTS
celery                     "celery -A core work…"   celery              running
core                       "/bin/sh -c 'python …"   core                running             0.0.0.0:8000->8000/tcp
cornerpos-default-core-1   "python3"                default-core        exited (0)
cornerpos-selenium-1       "/opt/bin/entry_poin…"   selenium            running             0.0.0.0:4444->4444/tcp, 0.0.0.0:5900->5900/tcp
redis                      "docker-entrypoint.s…"   redis               running             0.0.0.0:6379->6379/tcp
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
This project is configured with a Selenium node. If you want to look how interact with a browser please use your prefer viewer. We recomended [VNC](https://www.realvnc.com/es/connect/download/viewer/) and connect with localhost:5900 | password:

https://user-images.githubusercontent.com/1699198/134784450-07904c0b-d91b-46aa-b4f2-e709d7eab9cd.mp4
___
## Slack Notification by CornerBot:
https://user-images.githubusercontent.com/1699198/134784598-fe665a55-af50-4d7c-ba11-b12aebcba30e.mov
___
