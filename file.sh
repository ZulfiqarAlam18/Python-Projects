#!/bin/bash

echo -n "Enter file namne"
read filename

if [ -e "$filename" ]; then
    echo "$filename exists."
else
    echo "$filename does not exist."
fi
