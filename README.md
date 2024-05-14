# outils_traitement_corpus
Projet pour le cours d'outils de traitement de corpus 
## Alix Sirven-Viénot M1 TAL (Nanterre) 


## Semaine 1 
### Choix du corpus de référence 
Pour le choix du corpus, j'ai choisi de reproduire ce dataset de la loi japonaise. 
- [ ] après discussion avec une amie en droit besoin de plus de ressource pour la recherche d'information dans les textes de loi 

https://huggingface.co/datasets/y2lan/japan-law
-> loi japonaise 
Ce dataset contient 5 colonnes: 
- num : le numéro de la loi (e.g., Reiwa 5th Year Pollution Adjustment Committee Rule No. 1)
- title : le titre de la loi 
- id : son identifiant unique
- date: sa date de mise en effet 
- body : le texte  de la loi en entier


La licence de ce dataset appartient au mit
Il a été créé pour perfomer les taches suivantes:
  - summarization
  - text-generation
  - question-answering
Il est entièrement en japonnais
Il contient 8.75k textes de lois (1K<n<10K)
la dernière modification de ce coprus date du 1er Aout 2023, il s'agissait de la déduplication des données.


### Création du corpus 

Pour recréer un de ces corpus, j'ai trouvé ce site qui regroupe les codes du droit français aux formats pdf, rss et xml.  
https://codes.droit.org/  
Il contient les 78 codes de la loi française

En deuxième partie j'ai scraper les décisions de justices: 
Il y a aussi plusieurs sites qui regroupent des décisions de justice.   
Comme celui-ci filtrer pour les décisions de justices relevant uniquement du tribunal de commerce.    
https://justice.pappers.fr/recherche?juridiction[]=tribunaux+de+commerce -> Site protégé ne peux recupérer les données   

https://www.justice.gouv.fr/documentation/open-data-decisions-justice   
J'ai bien vérifié que toutes les décisions de justices soient bien en open source. 

Récupération des données sur le site internet du projet Judilibre:  
https://www.courdecassation.fr/acces-rapide-judilibre/open-data-et-api   
Voici le git du projet judilibre : 
https://github.com/Cour-de-cassation/judilibre-search/   
 

Ce corpus peut avoir plusieurs usages:   
- Il peut être utilisé pour des tâches de classification de textes
ex: Ordonnance / Décision de justice / de quel cours il s'agit ?  
- Pour entrainer des modèles à répondre à des questions
ex: Qui est le juge / Quels sont les avocats ? / Quand la desicion a-t-elle été rendu ? / Sur quel article de lois s'appuie cette décision ? Quel est le résultat de la décision ? ...   

Dans ce cas présent nous allons l'utiliser pour une tâche de classification. 
Il devra classer les articles selon 
- le code auquel il appartient
- s'il sagit d'une loi, d'une réglementation ou d'une annexe 



## Semaine 2 - Récupération des données 
Absente ce jour là, mais si j'ai a peu près compris:  
- récupération de données pour création du corpus  
- faire un script pour faire du scrapping (à partir d'un lien en récupérer plein)  
- donne un fichier CSV avec les colonnes de notre corpus final    

### Script de scrapping 
Ça marche! 
Pour commencer: récupération de tous les liens xml des codes. 
Puis récupération des infos pour chaque article de chaque code de lois 
Utilisation de Requests, Beautiful soup et de lxml.  
Beautiful soup très lent - bizzaroïde demandé si peut faire autre technique 

Pour le num des lois = chemin vers les lois (code > Partie (législative/réglementaire/annexes) > Livre nbr > Titre nbr > Chapitre nbr > article nbr ) 
Ajout de deux colonnes en plus que celui d'origine : 
- modTitle : le titre donné à la dernière modification de l'article (ex: décret numéro)
- code : le nom du code de loi auquel il appartient 

## Semaine 3 - Format Dataset
### Jupyter Notebook - TD_s3.ipynb
Création du format Dataset pour hugging face. -> notebook TD_s3.ipynb
Dataset({
    features: ['num', 'title', 'id', 'date', 'body'],
    num_rows: 3613
})

# Semaine 4 - Docker et que faire avec les données 
## Représentations des données 
Quelles mesures peuvent être utilisé pour ce projet ? 

## Docker 
Installation Réussi d'un docker dans le dossier ~/Documents/M1_TAL/outils
Il s'appelle flamboyant_leaky et c'est une alpine ! 
mdp : default password (Sinon je vais oublier c'est mon premier aussi)
Du coup faut mettre le corpus dedans ? 

# Semaine 5 - statistiques et mesures de corpus 
## Statistiques sur le corpus  
  
## Quels mesures peuvent être utilisé pour évaluer le corpus  


# Semaine 6 - 
## Division du corpus 
Test Dev Train   

## DataSet Card 
Doit contenir toutes les infos nécéssaire 
YAML -> déclaration et configuration


# AUTRE CORPUS 
https://huggingface.co/datasets/eckendoerffer/justice_fr?row=14
-> output = décision de justice / article de lois  
-> instructions = questions  
-> input = textes de lois   
