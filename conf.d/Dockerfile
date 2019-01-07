FROM python:3.5

LABEL maintainer="williamyan1024@gmail.com"

RUN pip install --no-cache-dir --upgrade --ignore-installed \
	aiohttp==3.4.1 \
	jinja2==2.10 \
	pymysql==0.9.2 \
	peewee==3.6.4 
	# MarkupSafe==1.0 \
	# async-timeout==3.0.0 \
	# attrs==18.1.0 \
	# chardet==3.0.4 \
	# idna==2.7 \
	# idna-ssl==1.1.0 \
	# multidict==4.3.1 \
	# yarl==1.2.6 \
	# asn1crypto==0.24.0 \
	# cffi==1.11.5 \
	# cryptography==2.3.1 \
	# pycparser==2.18 \
	# six==1.11.0

EXPOSE 7004

CMD ["python3"]

