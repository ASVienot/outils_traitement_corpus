# outils_traitement_corpus
Projet pour le cours d'outils de traitement de corpus 
## Alix Sirven-Viénot M1 TAL (Nanterre) 


## Semaine 1 
### Choix du corpus 
Pour le choix du corpus, je voudrais travailler sur un corpus touchant au droit.  
Sur hugging face, j'ai trouvé plusieurs corpus pouvant être intéressant à recréer. 
Ceux-ci portent surtout sur des taches de classification de texte, de génération de texte/summarisation ou de réponse à des questions.  

https://huggingface.co/datasets/eckendoerffer/justice_fr?row=14
-> output = décision de justice / article de lois  
-> instructions = questions  
-> input = textes de lois   

Decision de justice 
https://huggingface.co/datasets/arnavj007/justice-dataset
-> donne des infos sur comment la décision de justice a été prise  
-> quel est le type de decision, quel est la problematique, la date, le lieu, le parti ...   

Summaries of US court case 
https://huggingface.co/datasets/HartreeCentre/JustiaCorpus
-> Text2text generation 
-> summarization  

Question réponse (table question answering) et text generation 
https://huggingface.co/datasets/louisbrulenaudet/code-consommation?row=4
https://huggingface.co/datasets/louisbrulenaudet/code-disciplinaire-penal-marine-marchande?row=4
-> existe plusieurs versions  

Classification de texte sur des documents légaux 
https://huggingface.co/datasets/DoctrineAI/legal_document_structuring?row=56 
-> taille de la police, italic, gras
-> récuperer de documents pdf et html et donner leur structure hiérarchique    

https://huggingface.co/datasets/AdaptLLM/law_knowledge_prob?row=10
-> pas tout compris mais ça a l'air top 
-> donne un thème à la décision de justice ?  

Court Européenne des droits de l'homme  
https://huggingface.co/datasets/glnmario/ECHR  
-> donne le résultat de la décision de justice (0 ou 1)  
-> Infos sur le doc, noms des juges, conclusion...  


### Création du corpus 
Pour recréer un de ces corpus, j'ai trouvé ce site qui regroupe les codes du droit français en pdf, rss et xml.
https://codes.droit.org/  

Il y a aussi plusieurs sites qui regroupent des décisions de justice.   
Comme celui-ci filtrer pour les décisions de justices relevant uniquement du tribunal de commerce.    
https://justice.pappers.fr/recherche?juridiction[]=tribunaux+de+commerce -> Site protégé ne peux recupérer les données   

https://www.justice.gouv.fr/documentation/open-data-decisions-justice -> toutes les décisions de justices sont en open source 

Récupération des données sur Judilibre:  
https://www.courdecassation.fr/acces-rapide-judilibre/open-data-et-api  
https://github.com/Cour-de-cassation/judilibre-search/ -> git du projet judilibre  


But du corpus:  
- classification de texte ?   
Ordonnance / Décision de justice / de quel cours il s'agit ?  
- Réponse à des questions  
Qui est le juge / Quels sont les avocats ? / Quand la desicion a-t-elle été rendu ? / Sur quel article de lois s'appuie cette décision ? Quel est le résultat de la décision ? ...   
- donner l'article de loi sur lequel s'appuie la décision  


## Semaine 2 - Récupération des données 
Absente ce jour là, mais si j'ai a peu près compris:  
- récupération de données pour création du corpus  
- faire un script pour faire du scrapping (à partir d'un lien en récupérer plein)  
- donne un fichier CSV avec les colonnes de notre corpus final ?   

### Script de scrapping 
Bon ... c'est un début.


## Semaine 3 - Format Dataset
### Jupyter Notebook - TD_s3.ipynb
Création du format Dataset pour hugging face ? 

# Semaine 4 - Docker et que faire avec les données 
## Représentations des données 
Quelles mesures peuvent être utilisé pour ce projet ? 

## Docker 
Installation Réussi d'un docker dans le dossier ~/Documents/M1_TAL/outils
Il s'appelle flamboyant_leaky et c'est une alpine ! 
mdp : default password (Sinon je vais oublier c'est mon premier aussi)
Du coup faut mettre le corpus dedans ? 