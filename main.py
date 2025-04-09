import requests
from bs4 import BeautifulSoup
import csv
def scrapp(motclef):
    reponse=0
    if __name__ =='__main__':
        dejaecris=[]
        #print (True)
        url=['https://www.francetvinfo.fr/monde/russie/']
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

        for lien in url :

                page=requests.get(lien,headers=headers)
                good=BeautifulSoup(page.content,'html.parser')
                p=good.find_all('p')

                with open('donnes.csv','r') as fichier:
                    lecture=csv.reader(fichier)
                    entete=next(lecture)
                    for i in lecture:
                        dejaecris.append(i)
                        print(dejaecris)


                for i in p:
                    txt=i.get_text()
                    if motclef in txt and [lien,txt] not in dejaecris:
                        with open('donnes.csv','a') as fichier:
                            ecriture=csv.writer(fichier)
                            ecriture.writerow(entete)
                            ecriture.writerow([lien,txt])


print(scrapp('uk'))