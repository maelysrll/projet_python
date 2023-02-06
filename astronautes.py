import requests
from pprint import pprint

astro= requests.get("http://api.open-notify.org/astros.json").json()

# afficher la liste des astronautes actuellement dans l'espace
for personne in astro["people"]:
    if personne["craft"] == "ISS":
        print(personne)

