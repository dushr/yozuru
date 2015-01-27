#!/bin/bash

YUM_CMD=$(which yum)
APT_GET_CMD=$(which apt-get)

if [ "$(id -u)" != "0" ]; then
	echo "Sorry, you are not root. Run this script as root or with sudo"
	exit 1
fi

if [[ ! -z $YUM_CMD ]]; then
    yum update -y
    yum groupinstall "Development Tools"
    yum install python27-devel python-pip python-setuptools
    pip install --upgrade pip
    pip install virtualenv
elif [[ ! -z $APT_GET_CMD ]]; then
    apt-get -y update && apt-get -y upgrade
    apt-get python-dev build-essential python-pip
    pip install --upgrade pip
    pip install virtualenv
elif [[ ! -z $OTHER_CMD ]]; then
    echo "This os don't have apt-get or yum installed."
else
    echo "error can't install package."
exit 1;
fi