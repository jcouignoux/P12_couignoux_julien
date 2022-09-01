# P12_couignoux_julien

![](docs/logo.png)
***

## Sommaire

* [I. Introduction](#chapter1)
    * [Description](#section1_1)
    * [Objectif](#section1_2)
* [II. Installation](#chapter2)
    * [Technologies utilisées](#section2_1)
    * [Usage](#section2_2)
    * [Note](#section2_3)
* [III. Application usage](#chapter3)

***
## I. Introduction <a class="anchor" id="chapter1"></a>

Epic Events est une entreprise de conseil et de gestion dans l'événementiel qui répond aux besoins des start-up voulant organiser des « fêtes épiques ».

### Description <a class="anchor" id="section1_1"></a>
Une application de gestion de la relation client (CRM) de l'entreprise, qui effectue le suivi de tous les clients et événements.

### Objectif <a class="anchor" id="section1_2"></a>
Développer une application sécurisée suite à une compromission de l'intégrité des informations.
***

## II. Installation <a class="anchor" id="chapter2"></a>

### Technologies utilisées <a class="anchor" id="section2_1"></a>
* Python 3  
* Django 4  
* Django Rest Framework   
* PostgreSQL  

### Usage <a class="anchor" id="section2_2"></a>
* Installer python 3: https://www.python.org/downloads/
* Créer et activer un environnment virtuel: https://docs.python.org/3/library/venv.html
* Installer les prérequis: pip install -r requirements.txt
* Cloner le projet depuis github: [git clone git@github.com:jcouignoux/P12_couignoux_julien.git](git@github.com:jcouignoux/P12_couignoux_julien.git)
* python django_web_app/manage.py makemigrations
* python django_web_app/manage.py migrate
* python django_web_app/manage.py runserver
* In your web browser enter the address : http://localhost:8000/projects/ or http://127.0.0.1:8000/projects/

### Note <a class="anchor" id="section2_3"></a>
The Secret_Key required for the execution and debugging of project is not removed from the project code. So you can use the project as your college mini-project or by using the project code you can build your own project.
