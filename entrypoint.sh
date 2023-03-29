#!/bin/bash
gunicorn -w 4 -b 0.0.0.0 'prowessive.app:app' --pythonpath "prowessive"
