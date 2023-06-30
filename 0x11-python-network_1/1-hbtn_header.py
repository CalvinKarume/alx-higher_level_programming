#!/usr/bin/python3
"""Fetches a URL, extracts the X-Request-Id from the response header, and displays it."""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
