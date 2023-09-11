#To activate venv: source venv/bin/activatepython

#References: Used ChatGPT for basic syntax

import requests

site = 'https://raw.githubusercontent.com/woodepic/CMPUT_404_Labs/main/Lab1/print_requests_version.py'
response = requests.get(site)
print(response.text)