#!/usr/bin/python3
"""
 Python script that takes in a URL and an email, sends a POST request to the
 passed URL with the email as a parameter, and displays the body of the
 response (decoded in utf-8)
 """

if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys

    values = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(values).encode('ascii')
    request = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(request) as response:
        html = response.read()
        print(html.decode('utf-8'))
