# Projet base de donnée MongoDB

## Consignes

1. Avoir minimum deux sources de données. Dont, au moins, une en temps réel.
2. Faire une interface pour pouvoir tester les opérations CRUD :
    - CREATE : Un formulaire où je peux ajouter un document dans la base.
    - READ : Formulaire où je peux selectionner un document en fonction d’une clé.
    - UPDATE : Formulaire où je peux update une ligne en fonction d’un id.
    - DELETE : Formulaire où je peux delete une ligne en fonction d’un id
3. Un bouton qui mettera à jour la source de donnée en temps réel. En affichant la réponse de l’API et documents ajoutés à la base.
4. Faire un fichier __Read Me__.

## Le projet

La planète est raversée par des tremblements de terre. Pouvons-nous les prévoir ou voir les effets de leur passage par la météo ? Nous étudions la météos du lieu de tremblement de terre pour, peut-être, y trouver une corrélation.  

## Outils utilisés

- Trello : Application de la méthode agile et organisation.
- Github : dépôt, mettre en commun et rendu.
- Python, Flask (HTML-CSS) et divers librairies : Interface et programmation
- MongoDB : Base de donnée

### Installer les librairies

Vous trouverez les façon d'installer les librairies dans les fichiers même, en commentaire dans la partie dédié à leur importation. 

### API et fichiers 

Pour les API :
- Quelles sont les données de l’API (pourquoi cette API)
- Les paramètres possibles
- La réponse et les clés possibles

Pour les fichiers :
- Quels sont les données de ce fichier (pourquoi ce/ces fichier)
- Les colonnes et leur utilité

## Installation

Clonez le projet sur votre ordinateur.

### Environnement

Copier le fichier .env.example en .env et le remplir avec vos informations.
API_KEY correspond à la clé API de weatherapi 

https://www.weatherapi.com/

### Données

Pour remplir la base de données, il faut lancer le script de récupération de données historique (qui récupère un mois de données).
    
```python create_historic_data.py```

Un processus de récupération de données puis d'agrégation est lancé.

### Backend (Flask)
Installez les dépendances python

```pip install -r requirements.txt```

Lancez le serveur

```python main.py```

### Client frontend (vue.js)
Installez les dépendances npm

```cd dashboard && npm install```

Lancez le client 

```cd dashboard && npm run dev```

## Utilisation de l'interface

## L'équipe

Nous employons la méthode agile (Voir "outils utilisés" pour plus de détail.).

- Axel
- Yassine
- Hichem
- Lucas G.