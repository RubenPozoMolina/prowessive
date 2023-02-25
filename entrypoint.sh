#!/bin/bash
gunicorn -w 4 -b 0.0.0.0 'app:app'
#while :; do sleep 10; done
