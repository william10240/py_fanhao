FROM python:3.5

LABEL maintainer="williamyan1024@gmail.com"


COPY start.sh /run/start.sh

RUN echo 'deb http://mirrors.aliyun.com/debian stretch main \n\
deb http://mirrors.aliyun.com/debian stretch-updates main \n\
deb http://mirrors.aliyun.com/debian-security stretch/updates main' > /etc/apt/sources.list \
	&& apt-get update \
	&& apt-get install -y --allow-unauthenticated build-essential polipo \
	&& wget https://github.com/jedisct1/libsodium/releases/download/1.0.10/libsodium-1.0.10.tar.gz \
	&& tar -zxvf libsodium-1.0.10.tar.gz && cd libsodium-1.0.10 \
	&& ./configure && make -j4 && make install \
	&& echo /usr/local/lib > /etc/ld.so.conf.d/usr_local_lib.conf \
	&& ldconfig \
	&& chmod +x /run/start.sh

RUN pip install --no-cache-dir --upgrade --ignore-installed -i https://mirrors.aliyun.com/pypi/simple/ \
	aiohttp==3.4.1 \
	jinja2==2.10 \
	pymysql==0.9.2 \
	peewee==3.6.4 \
	https://github.com/shadowsocks/shadowsocks/archive/master.zip -U
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


EXPOSE 27004

CMD ["python3"]

