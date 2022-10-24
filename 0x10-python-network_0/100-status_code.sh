#!/bin/bash
# sends a request to a URL passed as an argument then displays the status code response
curl -s -o /dev/null -w "%{http_code}" "$1"
