import pandas as pd
import matplotlib.pyplot as plt
import spacy
import csv
from collections import Counter

nlp = spacy.load("fr_core_news_sm")


def most_common_words_per_code(data):
    """ 
    Cette fonction prend le dataset des articles de lois et retourne une liste de dictionnaires contenant en clef le code et en valeur une liste de tuple des mots les plus courant dans ce code de loi. 
    Parameters: 
    -----------
    data : dataset
        a dataset of the articles of the French law  
    Returns: 
    --------
    dico_code_mots : dict 
        a dictionnary of codes with their list of tuples of most common words and their frequency.
    """
    dico_code_mots = {}
    for code, group in data.groupby('code'):
        # Preprocess text for each code
        preprocessed_article = group['body'].apply(traitement)
        # Flatten the list of tokens
        tokens = [token for sublist in preprocessed_article for token in sublist]
        # Count the occurrence of each word
        word_counts = Counter(tokens)
        # Get the 5 most common words
        common_words = word_counts.most_common(10)
        dico_code_mots[code] = common_words
    return dico_code_mots


def traitement(article):
    """ 
    Cette fonction prend le texte des articles de lois et retourne l'article ayant surbis un prétraitement. 
    Le prétraitement consiste à retirer: les stopwords, les chiffres, les urls, les espaces, les ponctuations et les mots de moins de deux charactères (afin d'enlever les "l", "R" et "L." et "R." etc.).    
    Parameters: 
    -----------
    article : str
        a string of the text of the laws  
    Returns: 
    --------
    article : str 
        a list of str of the words present in the law after treatement
    """
    doc = nlp(article)
    article = [token.text for token in doc if (not token.is_punct) and (not token.is_space) and (not token.is_digit) and (not token.like_url) and (not token.is_stop) and len(token)>2]
    return article

def hop_en_csv(code_mots):
    """ 
    Cette fonction prend le dico des codes avec une liste de dictionnaires contenant en clef le code et en valeur une liste de tuple des mots les plus courant dans ce code de loi.des articles de lois et retourne l'article ayant surbis un prétraitement. 
    Parameters: 
    -----------
    article : str
        a string of the text of the laws  
    Returns: 
    --------
    article : str 
        a list of str of the words present in the law after treatement
    """  
    rows =[]
    for code, mots in code_mots.items(): 
        for mot, count in mots: 
            rows.append({'code': code, 'mot': mot, 'freq': count})
    with open("../data/freq_mots_10.csv", mode='w', newline ='') as fichier:
        writer = csv.DictWriter(fichier, fieldnames=['code', 'mot', 'freq'])
        writer.writeheader()
        writer.writerows(rows)

def main(): 
    data = pd.read_csv("../data/annotation_10.csv")
    common_words_per_code = most_common_words_per_code(data)
    hop_en_csv(common_words_per_code)
    for code, common_words in common_words_per_code.items():
        print(f"Code: {code}")
        for word, count in common_words:
            print(f"{word}: {count}")

if __name__ == '__main__':
    main()