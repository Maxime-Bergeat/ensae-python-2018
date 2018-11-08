#!/home/samuel/anaconda3/bin/python

import requests
import urllib
import bs4
import os

from urllib import request

os.chdir("C:/Users/maxim/Documents/ensae-python-2018/Data")
fichier_url = open("liste_urls_haikus_auteurs_franco_V2_20181022.csv", "r")
url = fichier_url.read().split("\n")
fichier_url.close()


def scrapper_sur_csv() :
	"""Écrit chaque haiku sur une ligne dans le fichier haikus.csv"""
	haikus = open("haikus.csv", "w")
	
	i = 1
	while i < len(url)-1 :
		url_page = url[i].split(",")[1]
		print(url_page)
		page = request.urlopen(url_page).read()
		page = bs4.BeautifulSoup(page, "lxml")
		extrait = page.findAll('p', {'class' : 'dbhkanahaiku'})
		extrait = str(extrait) # on convertit l'objet BS en chaîne de caractères
		extrait = extrait.split('class="dbhkanahaiku">')[1] #On retire la balise initiale
		extrait = extrait.replace("</p>]", "") #On retire la balise finale
		extrait = extrait.replace("<br/>","")
		extrait = extrait.replace("\r", "")
		extrait = extrait.split("\n\n")
		auteur = page.findAll('p', {'class' : 'dbhktlref'})
		auteur=str(auteur)
		auteur = auteur.split("<br/>")[1]
		pays = auteur.split(",")[1]
		auteur = auteur.split(",")[0]
		j = 0
		while j < len(extrait) :
			haiku = extrait[j].replace("\n", "\\\\")
			haiku = haiku + "\n\n\n"
			#print("On va écrire ça :", haiku)
			print(round(100*i/(len(url)-1),1), "%")
			texte = auteur + " | " + pays + " | " + haiku
			haikus.write(texte)
			j += 1
		i += 1
	haikus.close()
scrapper_sur_csv()


### Pb sur le le haïkus de l'auteur 15
def test() :
	i = 15
	url_page = url[i].split(",")[1]
	page = request.urlopen(url_page).read()
	page = bs4.BeautifulSoup(page, "lxml")
	extrait = page.findAll('p', {'class' : 'dbhkanahaiku'})
	extrait = str(extrait) # on convertit l'objet BS en chaîne de caractères
	extrait = extrait.split('class="dbhkanahaiku">')[1] #On retire la balise initiale
	extrait = extrait.replace("</p>]", "")#On retire la balise finale
	extrait = extrait.replace("<br/>","")
	extrait = extrait.replace("\r", "")
	extrait = extrait.split("\n\n")
	auteur = page.findAll('p', {'class' : 'dbhktlref'})
	auteur=str(auteur)
	auteur = auteur.split("<br/>")[1]
	pays = auteur.split(",")[1]
	auteur = auteur.split(",")[0]
	print("auteur :", auteur)
	haiku = extrait[0].replace("\n", "\\\\")
	haiku = haiku + "\n\n\n"
	print(haiku)

#test()

