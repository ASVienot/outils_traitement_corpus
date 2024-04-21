from dataclasses import dataclass
from bs4 import BeautifulSoup
import argparse

def ouverture_fichiers(fichier):
    with open(fichier, "r") as fp:
        donnees = fp.read()
        soup = BeautifulSoup(donnees, 'html.parser')
        return soup 


def main(fichier:str): 
    soup = ouverture_fichiers(fichier)
    


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("fichier", help="Donne un fichier html / xml à lire")
    args = parser.parse_args()

