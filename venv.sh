#!/usr/bin/env bash

usage() {
  echo "Usage: source $0"
  echo "A script that sets up a Python Virtualenv"
  exit 1
}

[ "$1" = "-h" ] && usage

version="$(<.python-version)"
IFS="." read -r major minor _ <<< "$version"

python=python"$major"."$minor"
pip=pip"$major"."$minor"

if ! python"$major"."$minor" --version | grep -q "Python $major.$minor" ; then
  echo "Please use pyenv and install Python $major.$minor"
  return
fi

"$python" -m venv venv
"$pip" install -r requirements.txt

source venv/bin/activate
