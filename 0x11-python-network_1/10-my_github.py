#!/usr/bin/python3
"""
Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""

if __name__ == "__main__":
    from requests import get, auth
    import sys
    url = 'https://api.github.com/user'
    user = sys.argv[1]
    password = sys.argv[2]
    req = get(url, auth=auth.HTTPBasicAuth(user, password))
    print(req.json().get('id'))
