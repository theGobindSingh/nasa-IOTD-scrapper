import os
import requests #pip install requests
import json

folder_name="nas_scr"     #This folder will be created in Documents

docs = os.path.expanduser("~/Documents").replace("\\","/") + "/"

try:
    os.mkdir(docs+folder_name)
except:
    print("")

loc = docs+folder_name
print ("save location: "+loc)
url_base="https://www.nasa.gov/api/2/ubernode/"

uNum=[470022,470016,469987,469945,469909,469849,469816,469620,469738,469627,469619,469571,469478,469416,469211,469253,469179,469209,469178,469142]

for x in uNum:
    r = requests.get(url_base+str(x))
    js=json.loads(r.text)
    il= str (((js["_source"])["master-image"])["uri"])
    il= il.replace("public://","https://www.nasa.gov/sites/default/files/")

    with open(os.path.join(loc,str(x)+".png"),"wb") as f:
        f.write(requests.get(il).content)
