
""" Scraping_code_lois
Ce script prend l'url contenant les codes du droits français et extrait les liens des fichiers xml qu'elle contient. 
Puis, elle crée un tableau contenant pour chaque article des différent codes, le num (arborescence suivant l'endroit d'ou vient l'article), le titre de l'article, son id, sa date de prise d'effet, le code dans lequel il est, son nom de modification et son body (texte de l'article).  
Ce script necessite les librairies: requests, lxml.html, BeautifulSoup de bs4, collections et csv. 
"""


# Téléchargement des librairies 
import requests
import lxml.html
from collections import namedtuple
from bs4 import BeautifulSoup
import csv

def get_urls(balises_liens):
    """
    Cette fonction prend une liste de balise de liens vers les codes et retourne la liste des urls dont on a besoin. 
    Parameters:
    ------
    balises_liens : list 
        a list of urls balises 
    Returns: 
    ------
    url_list : list 
        a list of strings containing the urls we need 
    """
    url_list = []
    for element in balises_liens:
        href = element.attrib['href']
        if href.startswith('http://') or href.startswith('https://'): 
            # vérifie que les liens appartiennent au même site 
            # url_list.append(href)
            pass
        elif href.startswith('/'):
            url_list.append('https://codes.droit.org/' + href)
        else:
            url_list.append('https://codes.droit.org/' + href)
        
    return url_list

def get_lois(url_list, Loi): 
    """
    Cette fonction prend une liste de liens vers les codes et retourne une liste d'object Loi.  
    Parameters:
    ------
    url_list : list 
        a list of urls  
    Loi : object type Loi (a namedtuple)
    Returns: 
    ------
    url_list : list 
        a list of object Loi 
    """
    liste_lois = []

    for url in url_list:
        req = requests.get(url)
        code_texte = req.text
        code_soup = BeautifulSoup(code_texte, 'xml')
        
        nom_code = code_soup.code['nom']
        
        articles = code_soup.find_all('article') # Trouve les articles et les mets dans un liste sur laquelle on itère  
        for article in articles:
            l_num = article['num']
            parents = [parent['title'] for parent in article.parents if parent.get('title')]
            titres_parents = " > ".join(reversed(parents))
            num = f"{nom_code} > {titres_parents} > {l_num}"
            title = f"{l_num} du {nom_code}"
            id = article['id']
            date = article['date']
            body = article.text
            code = nom_code
            mod_title = article.get('modTitle', None)

            loi = Loi(num, title, id, date, code, mod_title, body)
            #print(loi)
            liste_lois.append(loi)
    return liste_lois

def main ():
    # url = "https://codes.droit.org/"
    # r = requests.get(url)

    # root = lxml.html.fromstring(r.content)
    # balises_liens = root.xpath('//dd/a[3]') # trouver les balises contenant les liens
    # # la troisième balise a car les deux premières contiennent les liens pdf et rss

    url_list = ['https://codes.droit.org/payloads/Code%20civil.xml', 'https://codes.droit.org/payloads/Code%20g%C3%A9n%C3%A9ral%20des%20imp%C3%B4ts.xml','https://codes.droit.org/payloads/Code%20de%20justice%20militaire%20%28nouveau%29.xml', 'https://codes.droit.org/payloads/Code%20des%20ports%20maritimes.xml', 'https://codes.droit.org/payloads/Code%20des%20postes%20et%20des%20communications%20%C3%A9lectroniques.xml', 'https://codes.droit.org/payloads/Code%20de%20la%20route.xml', 'https://codes.droit.org/payloads/Code%20du%20sport.xml', 'https://codes.droit.org/payloads/Code%20du%20travail.xml', 'https://codes.droit.org/payloads/Code%20de%20l%27action%20sociale%20et%20des%20familles.xml', 'https://codes.droit.org/payloads/Code%20de%20la%20sant%C3%A9%20publique.xml']    
    #url_list = get_urls(balises_liens)
    print(len(url_list))
    
    Loi = namedtuple('Loi', ['num', 'title', 'id', 'date', 'code', 'mod_title', 'body'])
    # mettre toutes les infos dans l'objet loi 
    liste_lois = get_lois(url_list, Loi)

    # Remplir un Fichier csv avec les informations données dans les objets Loi 
    with open('../data/raw_codes_10.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(Loi._fields)
        for loi in liste_lois:
            writer.writerow(loi)
    


if __name__ == '__main__':
    main()