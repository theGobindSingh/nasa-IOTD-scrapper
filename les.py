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

for x in range(0,20):
    url_main="https://www.nasa.gov/api/2/ubernode/_search?size=24&from=0&sort=promo-date-time%3Adesc&q=((ubernode-type%3Aimage)%20AND%20(routes%3A1446))&_source_include=promo-date-time%2Cmaster-image%2Cnid%2Ctitle%2Ctopics%2Cmissions%2Ccollections%2Cother-tags%2Cubernode-type%2Cprimary-tag%2Csecondary-tag%2Ccardfeed-title%2Ctype%2Ccollection-asset-link%2Clink-or-attachment%2Cpr-leader-sentence%2Cimage-feature-caption%2Cattachments%2Curi"
    m=requests.get(url_main)
    mjs=json.loads(m.text)
    il=str(mjs["hits"]["hits"][x]["_source"]["master-image"]["uri"])
    il= il.replace("public://","https://www.nasa.gov/sites/default/files/")

    with open(os.path.join(loc,str(x)+".png"),"wb") as f:
        f.write(requests.get(il).content) 
    f.close()
