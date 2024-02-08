#!/bin/bash

echo -n "Enter User Name:"
read uname
echo -n "Enter User Password:"
read userpass


valid_username="zulfiqar"
valid_password="sdc"


# Extract the username and password from the arguments
input_username=$1
input_password=$2

# Verify the credentials
if [ "$uname" = "$valid_username" ] && [ "$userpass" = "$valid_password" ]; then
    echo "Login successful. Welcome, $valid_username!"
else
    echo "Login error. Invalid username or password."
fi
