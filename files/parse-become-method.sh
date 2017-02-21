#!/bin/sh

last=$1
shift
for i; do
  last="$1"
  shift
done

if test ":$last" = ":--FAKE::::COMMAND=$PPID"; then
  echo -n NO-BECOME
else
  set -- $last
  echo -n "${1:-sudo}"
fi
