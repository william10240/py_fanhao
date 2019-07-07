#!/bin/sh

/usr/local/bin/sslocal -c /app/conf.d/shadowsocks.json --libsodium=/usr/local/lib/libsodium.so -d start

/usr/sbin/service polipo restart

python3.5 /app/app.py
