#!/bin/bash

echo -n "Enter first String:"
read string1
echo -n "Enter Second String:"
read string2

# Compare the strings
if [ "$string1" = "$string2" ]; then
    echo "The strings are equal."
else
    echo "The strings are not equal."
fi
