#!/bin/bash

cd /opt/ctf/ponypoem/rw

if [[ "i386" == "x86_64" ]] || [[ "x86_64" == "x86_64" ]] ; then
  ../ro/ponypoem 2>/dev/null
else
  qemu-x86_64 ../ro/ponypoem 2>/dev/null
fi