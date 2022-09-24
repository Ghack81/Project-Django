# Projet Django
Structure M.V.T. avec Django
Django est basé sur l’architecture MVT (Model-View-Template). 
MVT est un modèle de conception de logiciel permettant de développer une application Web.

La structure MVT comprend les trois parties suivantes :

Modèle : Le modèle va agir comme l’interface de vos données. Il est responsable de la maintenance des données. C’est la structure de données logique derrière l’ensemble de l’application et elle est représentée par une base de données (généralement des bases de données relationnelles telles que MySql, Postgres). 

Vue : La vue est l’interface utilisateur — ce que vous voyez dans votre navigateur lorsque vous affichez un site Web. Il est représenté par des fichiers HTML/CSS/Javascript et Jinja. 

Template : Un template se compose de parties statiques de la sortie HTML souhaitée ainsi que d’une syntaxe spéciale décrivant comment le contenu dynamique sera inséré. 

![image](https://user-images.githubusercontent.com/78435787/192114202-82bcb8db-dc4d-43d0-a35c-825ac700eb64.png)
![image](https://user-images.githubusercontent.com/78435787/192114396-e0dd8686-7072-4ea0-9dcf-c91d7c4db1a9.png)


# Structuration du projet :
Un projet Django lorsqu’il est initialisé contient par défaut des fichiers de base tels que manage.py, view.py, etc. 
Une structure de projet simple suffit pour créer une application d’une seule page. 
Voici les principaux fichiers et leurs explications. Dans le dossier myproject (dossier du projet), il y aura les fichiers suivants :

manage.py- Ce fichier est utilisé pour interagir avec votre projet via la ligne de commande (démarrer le serveur, synchroniser la base de données… etc). 
Pour obtenir la liste complète des commandes pouvant être exécutées par manage.py, tapez ce code dans la fenêtre de commande. 

$ python manage.py help

dossier ( myproject ) – Ce dossier contient tous les packages de votre projet. Initialement, il contient quatre fichiers :

1) _init_.py – Il s’agit d’un package python. Il est appelé lorsque le package ou un module du package est importé. Nous l’utilisons généralement pour exécuter le code d’initialisation du package, par exemple pour l’initialisation des données au niveau du package.

2) settings.py – Comme son nom l’indique, il contient tous les paramètres du site Web. Dans ce fichier, nous enregistrons toutes les applications que nous créons, l’emplacement de nos fichiers statiques, les détails de configuration de la base de données, etc.

3) urls.py – Dans ce fichier, nous stockons tous les liens du projet et les fonctions à appeler.

4) wsgi.py – Ce fichier est utilisé pour déployer le projet dans WSGI. Il est utilisé pour aider votre application Django à communiquer avec le serveur Web.




