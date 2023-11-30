#!/bin/bash
#Takes in a URL, sends a request that to URL,displays the size of the body of the response
curl -s "$1" | wc -ci
