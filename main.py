import requests
import os 

with open(".env", "r") as f:
    api_key = f.read().strip()

URL = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

try:
    res = requests.get(URL)
    res.raise_for_status() 
    data = res.json()
    print(data.get("explanation", "Pas d'explication disponible."))
    if(data["media_type"] == "image" ):
        urlImage = data["hdurl"]
        image = requests.get(urlImage)

        chemin = os.path.expanduser("~/.config/fastfetch/image.jpg")
        chemindes = os.path.expanduser("~/.config/fastfetch/nasa_desc.txt")

        with open(chemin, "wb") as f: 
            f.write(image.content)
        desc = data.get("explanation","")
        desc = (desc[:150]+"...") if len(desc) > 150 else desc
        with open(chemindes,"w") as d:
            d.write(desc)

except requests.exceptions.HTTPError as err:
    print(f"Erreur HTTP : {err}")
except Exception as e:
    print(f"Une erreur est survenue : {e}")


