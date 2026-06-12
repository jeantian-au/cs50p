import requests


def main():
    artist = input("Please insert your favorite artist: ")
    try:
        response = requests.get(
            "https://api.artic.edu/api/v1/artworks/search", {"q": artist}
        )
    except requests.HTTPError:
        print("couldn't get it due to internet error")
        return
    content = response.json()
    for artwork in content["data"]:
        print(f"-{artwork["title"]}")


main()
