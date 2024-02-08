#!/bin/bash

#check of ubundu

if [ -x "$(command -v isb_realease)" && [ "$(lsb_release -si)" ] ="Ubundu";
then 
sudo apt update
sudo apt upgrade -y
else

echo "Distribution not found"
exit 1

fi
