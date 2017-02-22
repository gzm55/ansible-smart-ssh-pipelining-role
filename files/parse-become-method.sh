#!/bin/sh

last=$1
shift
for i; do
  last="$1"
  shift
done

result=UNKNOWN-BECOME-METHOD
set -- $last
case "$1" in
(--FAKE::::COMMAND=$PPID) result=NO-BECOME ;;
(sudo|su|pbrun|pfexec|doas|dzdo|ksu) result="$1" ;;
esac

echo -n "$result"
