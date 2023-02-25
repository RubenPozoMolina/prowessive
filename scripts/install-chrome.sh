#!/bin/bash
curl -sS 'https://dl-ssl.google.com/linux/linux_signing_key.pub' | apt-key add -
echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
apt-get update -qqy
apt-get -qqy install google-chrome-stable
