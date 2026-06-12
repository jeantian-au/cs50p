import json
import sys
import requests

if len(sys.argv) != 2:
    sys.exit("which singer you want to checkout? ")

url = f"https://itunes.apple.com/search?entity=tvShow&term={sys.argv[1]}"
response = requests.get(url)
o = response.json()

for result in o["results"]:
    print(result["trackName"])
