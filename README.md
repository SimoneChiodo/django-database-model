# Progetto Django: Django Database Model

## 📖 Descrizione
**Django Database Model** è il proseguimento del progetto 
<a href="https://github.com/SimoneChiodo/hello-django.git">***Hello Django***</a>.  
In questo esercizio si esplora la gestione dei **modelli (Model)** e del **database** in Django, imparando a collegare i dati alle pagine HTML attraverso il **sistema ORM** (Object Relational Mapper).

L’obiettivo è creare un semplice modello `Post` e mostrare i dati dinamicamente nel sito web.


## 🌍 Funzionalità principali
- **Creazione del modello Post**: definizione di una classe `Post` con campi `titolo`, `contenuto` e `data_creazione`.  
- **Migrazioni del database**: esecuzione dei comandi `python manage.py makemigrations` e `python manage.py migrate` per sincronizzare il modello con il database.  
- **Inserimento dati**: creazione di record direttamente dalla **shell Django** (`python manage.py shell`).  
- **Visualizzazione dei post**: una pagina HTML mostra l’elenco di tutti i post salvati.  
- **Dettaglio post**: seconda pagina che mostra le informazioni di un singolo post selezionato.  


## 🎯 Obiettivo
Capire come funziona:
- l’**ORM di Django**,  
- il **processo di migrazione** dei modelli,  
- il **collegamento tra database, views e template** per generare contenuti dinamici.  


## 🛠️ Tecnologie utilizzate
- **Python** → linguaggio principale del progetto.  
- **Django** → framework per la gestione del database, delle view e del routing.  
- **SQLite** → database predefinito di Django, usato per lo sviluppo locale.  
- **HTML** → per visualizzare l’elenco e i dettagli dei post.  
