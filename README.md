PROJET FAKE NEWS DETECTION PYTHON

Le but de notre application est de déterminer la véracité d'une news avec comme données son titre et son contenu

Etat d'avancé du projet : 
Notre IA est entrainée, l'api fonctionne et nous renvoie la prediction ( vérifiée avec Insomnia ):

    0 - vrai news
    1 - fake news
Nous sommes au moment où nous devons connecter FASTAPI avec Django pour envoyer les données sur form à l'API

Vous pouvez retrouver le formulaire dans le fichier templates/main/index.html
Dans le fichier fakeNewsDetection/views.py on peut retrouver le début de code d'envoie des informations à FASTAPI

Vous pouvez retrouver le setup de FASTAPI dans le fichier main.py
ainsi que le model et le train vecteur dans /files

NB : Pour le moment nous utilisons uniquement l'information du titre de l'article pour savoir si la news est fake ou non
Nous avons également utilisé COLAB et non NOTEBOOK, voici le lien du colab ou vous êtes collaborateur : https://colab.research.google.com/drive/1IOesqqFhmqutIQzF_RgAT6e6HUnQQxQG#scrollTo=gsqDob7P19bu

DIMANCHE 23h59

GITHUB AJOUTER :
AGuyNextDoor ou Martin Vielvoye