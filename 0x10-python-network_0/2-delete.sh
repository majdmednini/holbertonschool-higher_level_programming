#!/bin/bash
# send a DELETE request to the URL passed as the first argument, displays the body of the response
curl -sLX DELETE "$1"
