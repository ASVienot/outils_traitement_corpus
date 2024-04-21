from dataclasses import dataclass
from bs4 import BeautifulSoup
import argparse

def lecture_lien(lien):
    #lire les liens pour pouvoir mettre un lien en argument 
    #surtout pour pouvoir lire les liens présent dans le doc1 et acceder à d'autres
    pass


def ouverture_fichiers(fichier):
    with open(fichier, "r") as fp:
        donnees = fp.read()
        soup = BeautifulSoup(donnees, 'html.parser')
        return soup 


def main(fichier:str): 
    soup = ouverture_fichiers(fichier)
    print(soup)

#but trouver les balises contenant des liens 
#ouvrir ses liens
#ouvrir avec soup et recommencer à trouver les balises contenant des liens etc... 



if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("fichier", help="Donne un fichier html / xml à lire")
    args = parser.parse_args()

