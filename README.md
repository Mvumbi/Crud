# 📚 Django CRUD - Gestion de livres

Ce projet est une application web développée avec **Django 5** permettant de gérer une collection de livres avec un système complet de **CRUD** (Créer, Lire, Modifier, Supprimer).

## 🚀 Fonctionnalités

- ➕ Ajouter un nouveau livre (titre, auteur, contenu)
- 📝 Modifier les livres existants
- 🔍 Voir les détails d’un livre
- 🗑 Supprimer un livre
- 📃 Liste des livres triés du plus récent au plus ancien
- 🎨 Interface responsive avec **Bootstrap 5**
- 🗃 Base de données : **SQLite** (par défaut)

## 🛠 Technologies utilisées

- [Python 3.12](https://www.python.org/)
- [Django 5.2.1](https://www.djangoproject.com/)
- [Bootstrap 5](https://getbootstrap.com/)
- [HTML5, CSS3](https://www.w3schools.com/html/html_css.asp)

## 📦 Installation locale

1. Cloner le dépôt :

```bash
git clone https://github.com/Mvumbi/crud.git
cd crud
```

2. Créer et activer un environnement virtuel :

windows:
```bash
python -m venv venv
venv\Scripts\activate
```
macOS/Linux :
```bash
python -m venv venv
source venv/bin/activate
```
3. Installer les dépendances :
```bash
pip install -r requirements.txt
```
4. Effectuer les migrations :
```bash
python manage.py migrate
```
5. Lancer le serveur Django:
```bash
python manage.py runserver
```
Le serveur sera accessible à l’adresse http://127.0.0.1:8000.