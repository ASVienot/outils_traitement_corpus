""" annotation_lois
Ce script prend le tableau des données sur les articles de lois "raw" et rajoute des colonnes d'annotation supplémentaires. 
Il prend comme argument le fichier raw_complet.csv. 
Il utilise les librairies

"""
# librairies 
import pandas as pd 
from datasets import load_dataset
import spacy
nlp = spacy.load('fr_core_news_sm') 


def lemmatization(body):
    """ 
    Cette fonction prend une chaine de caractères et retourne sa forme lemmatisée
    Parameters: 
    -----------
    body : str
            a string of the text of the laws  
    Returns: 
    --------
    lemma : list 
        a list of all the forms of the words present in the body 
    """
    doc = nlp(body)
    lemma = [token.lemma_ for token in doc]
    lemmes = ' '.join(lemma)
    return lemmes

def compte_mot(body):
    """ 
    Cette fonction prend une chaine de caractères et retourne son nombre de mots
    Parameters: 
    -----------
    body : str
            a string of the text of the laws  
    Returns: 
    --------
    nbr_mot : int 
        the number of words in the body 
    """
    doc = nlp(body)
    nbr_mot = len(doc)
    print(nbr_mot)
    return nbr_mot

def typage(title):
    """ 
    Cette fonction le nom de l'article et retourne sa première lettre si c'est A, D, L ou R et sinon elle retourne "autre".  
    Parameters: 
    -----------
    body : str
        a string of the name of the law  
    Returns: 
    --------
    type : str 
        A, D, L, R or "autre"
    """
    print(title)
    if title[0] not in ['A', 'D', 'L', 'R']:
        return "autre"
    else:
        return title[0]

def main(): 
    data = pd.read_csv("../data/X.csv")
    
    # Rajout colonne type d'article (L, R, D, A ou autre)
    data['type'] = data['title'].apply(typage)

    # Annotation morphosyntaxique? + nouvelle colonne lemma 
    #data['lemma'] = data['body'].apply(lemmatization)

    # Annotation du nombre de mots dans chaque article
    data['nbr_mot'] = data['body'].apply(compte_mot)

    data.to_csv("../data/X.csv", index=False)


if __name__ == '__main__':
    main()
