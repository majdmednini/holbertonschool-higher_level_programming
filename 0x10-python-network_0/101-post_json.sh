#!/bin/bash
# send a JSON POST request to a URL passed as the first argument then display the body of the response
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
