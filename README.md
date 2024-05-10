# outils_traitement_corpus
Projet pour le cours d'outils de traitement de corpus 
## Alix Sirven-Viénot M1 TAL (Nanterre) 


## Semaine 1 
### Choix du corpus 
Pour le choix du corpus, je voulais travailler sur un corpus touchant au droit.  
J'ai donc choisi de reproduire ce dataset de la loi japonaise. 

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


https://huggingface.co/datasets/eckendoerffer/justice_fr?row=14
-> output = décision de justice / article de lois  
-> instructions = questions  
-> input = textes de lois   


### Création du corpus 

Pour recréer un de ces corpus, j'ai trouvé ce site qui regroupe les codes du droit français aux formats pdf, rss et xml.  
https://codes.droit.org/  


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


## Semaine 2 - Récupération des données 
Absente ce jour là, mais si j'ai a peu près compris:  
- récupération de données pour création du corpus  
- faire un script pour faire du scrapping (à partir d'un lien en récupérer plein)  
- donne un fichier CSV avec les colonnes de notre corpus final    

### Script de scrapping 
Bon ... c'est un début.
Pour commencer: récupération de tous les liens xml des codes. 
Puis récupération des infos pour chaque article de chaque code de lois 



## Semaine 3 - Format Dataset
### Jupyter Notebook - TD_s3.ipynb
Création du format Dataset pour hugging face 

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