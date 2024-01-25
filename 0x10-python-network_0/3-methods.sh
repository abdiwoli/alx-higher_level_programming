#!/usr/bin/bash
#options
curl -sI "$1" -X OPTIONS | grep -i "Allow" | cut -d " " -f2-
