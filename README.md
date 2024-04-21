# outils_traitement_corpus
Projet pour le cours d'outils de traitement de corpus 
## Alix Sirven-Viénot M1 TAL (Nanterre) 


## Semaine 1 
### Choix du corpus 
Pour le choix du corpus, je voudrais travailler sur un corpus touchant au droit. Sur hugging face, j'ai trouvé plusieurs corpus pouvant être intéressant à recréer. 

Ceux-ci portent surtout sur de la classification de texte, de la génération de texte/summarisation ou de la reponse à des questions. 


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
https://justice.pappers.fr/recherche?juridiction[]=tribunaux+de+commerce
https://opendata.justice-administrative.fr/ -> ou celui-là 

https://www.justice.gouv.fr/documentation/open-data-decisions-justice -> toutes les décisions de justices sont en open source 



## Semaine 2 
Absente ce jour là, mais si j'ai a peu près compris: 
- récupération de données pour création du corpus 
- faire un script pour faire du scrapping (à partir d'un lien en récupérer plein)

### Récupération des données 


### Script de scrapping 
