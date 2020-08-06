#!/bin/sh

nohup /run/brook client -l 127.0.0.1:1080 -i 127.0.0.1 -s 000.000.000.000:00000 -p xxxxxxxxxx --http &

python3.5 /app/app.py
