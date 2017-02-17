#!/bin/sh

while test ":$#" != ":0" && test ":$1" != ":BECOME-HOST"; do
  shift
done

set -- $2
if test -n "$1"; then
  echo "$1"
  exit 0
fi

echo sudo
