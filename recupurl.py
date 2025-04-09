import requests
from bs4 import BeautifulSoup
import csv
from urllib.parse import urljoin
import urllib.robotparser
#python3 -m venv opcr
robots='https://www.francetvinfo.fr/robots.txt'
url='https://www.francetvinfo.fr'

def recupurl(robots,url):
    interdit=[]
    lien=[]
    verif=0
    dejaecris=[]
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

    with open('lien.csv','r') as fichier:
        lecture=csv.reader(fichier)
        for i in lecture:
            dejaecris.append(i)
    pracine=requests.get(robots,headers=headers)
    pracine=pracine.text.split('\n')
    for i in pracine:
        if i.startswith('Disallow: /'):
            path=i.split(':',1)[1]
            if urljoin(url,path) != url+'/' and path:
                interdit.append(urljoin(url,path))

    page=requests.get(url,headers=headers)
    contenu=BeautifulSoup(page.content,'html.parser')
    balise_a=contenu.find_all('a')
    for i in balise_a:
            verif=0
            href = i.get('href')
            txt=i.get_text()
            txt = urljoin(url, href)
            for t in interdit:
                    if txt not in interdit:
                        verif+=1
                
            if verif==len(interdit):
                    lien.append(txt)
    return lien,dejaecris
a=1
for i in recupurl(robots,url)[0]:
    a+=1
    with open('lien.csv','a') as fichier:
        ecriture=csv.writer(fichier)
        entete=['lien']
        ecriture.writerow(entete)
        ecriture.writerow([i])
print(recupurl(robots,url))
