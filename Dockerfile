FROM python:3.9

LABEL maintainer="williamyan1024@gmail.com"


RUN pip install --no-cache-dir --upgrade --ignore-installed -i https://mirrors.aliyun.com/pypi/simple/ \
	aiohttp \
	jinja2 \
	pymysql \
	peewee

