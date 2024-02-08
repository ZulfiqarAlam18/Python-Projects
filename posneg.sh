#!/bin/bash


#!/bin/bash

echo -n "Enter Any number"
read number

# Check if the number is positive, negative, or zero
if [ "$(echo "$number < 0" | bc)" -eq 1 ]; then
    echo "$number is negative."
elif [ "$(echo "$number > 0" | bc)" -eq 1 ]; then
    echo "$number is positive."
else
    echo "$number is zero."
fi


