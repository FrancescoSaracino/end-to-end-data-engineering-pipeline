[English](README.md) | [Italiano](README.it.md)

# Pipeline End-to-End di Data Engineering

## 📌 Panoramica

L’obiettivo è progettare e realizzare un flusso completo di gestione dei dati, coprendo l’intero ciclo di vita:
dall’ingestione e trasformazione dei dati, fino all’esposizione tramite API REST e alla visualizzazione tramite dashboard BI.

Il progetto è pensato come dimostrazione pratica di competenze fondamentali di **data engineering**, integrazione dei dati e analisi.

---

## 🏗️ Architettura del Progetto

La pipeline segue le seguenti fasi principali:

1. Ingestione di un dataset grezzo in formato CSV  
2. Trasformazione e analisi dei dati tramite Python  
3. Generazione di un dataset processato  
4. Caricamento dei dati in un database relazionale  
5. Esposizione dei dati tramite API REST  
6. Visualizzazione dei dati tramite Power BI  

---

## 🔄 Data Ingestion & ETL

La prima fase del progetto utilizza un **dataset pubblico in formato CSV** (`raw_data.csv`), memorizzato localmente.

Utilizzando **Python** e un approccio di **programmazione orientata agli oggetti**, il dataset grezzo viene pulito,
trasformato e analizzato.

Librerie principali utilizzate:
- **pandas** per la manipolazione e trasformazione dei dati  
- **scipy** per le analisi statistiche  
- **matplotlib** e **seaborn** per la visualizzazione esplorativa  

Attività principali:
- pulizia dei dati  
- trasformazioni (ad esempio conversione dei tipi di dato)  
- analisi esplorativa dei dati  

Al termine del processo ETL viene generato il file **`processed_data.csv`**.

> **Nota:** il caricamento del dataset processato nel database viene attualmente effettuato manualmente.  
> Per questo motivo la pipeline può essere considerata **semi-automatizzata**, con focus su trasformazione e analisi.

---

## 📊 Analisi Statistica

Sul dataset processato sono stati calcolati diversi **indici statistici descrittivi**  
e sono stati individuati **outlier** per le variabili quantitative.

Sono state inoltre condotte:
- **One-Way ANOVA**
- **Correlazione di Spearman**

per analizzare le relazioni tra specifiche variabili del dataset.

---

## 🗄️ Database & REST API

Il file **`processed_data.csv`** è stato importato in un **database MySQL** tramite **phpMyAdmin**
in ambiente locale (**XAMPP**).

A partire da questo database è stata sviluppata una **REST API** utilizzando **Flask (Python)**.

L’API espone diversi **endpoint GET** che interrogano direttamente il database e restituiscono i risultati in formato **JSON**.

La configurazione del database è gestita tramite **variabili d’ambiente (`.env`)**.
Le informazioni sensibili non sono versionate, seguendo le best practice backend.

Uno degli endpoint include anche una **semplice interfaccia frontend** per la consultazione dei dati.

---

## 📈 Data Visualization

A partire dal file **`processed_data.csv`** è stata realizzata una **dashboard Power BI**
per visualizzare i principali insight del dataset tramite grafici e indicatori.

---

## 📂 Struttura del Progetto

```text
project_root/
│
├── api/                 # Flask REST API
│   ├── requirements.txt
│   ├── app.py
│   └── ...
├── dataset/
│   ├── raw/
│   │   └── raw_data.csv
│   └── processed/
│       └── processed_data.csv
├── etl/                 # ETL & analisi statistica
│   ├── requirements.txt
│   └── pipeline/
│       ├── base_pipeline.py        # classe base
│       └── amazon_pipeline.py     # pipeline specifica (entry point)
├── bi/
│   └── dashboard.pbix              # Dashboard Power BI
└── db/
    └── schema.sql
```
---

## ▶️ Come Eseguire il Progetto (Setup Locale)

### Prerequisiti
- Python 3.9 o superiore  
- MySQL installato e in esecuzione  
- Virtual environment (consigliato)

### 1. Clonare il repository
Clona il repository del progetto e spostati nella directory principale del progetto.

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Configurare le variabili d’ambiente

All’interno della cartella `api`, creare il file `.env` partendo dall’esempio fornito.

```bash
cp api/.env.example api/.env
```

Modificare il file `.env` se necessario (nome database, utente, porta, ecc.).

### 3. Installare le dipendenze dell’API

Spostati nella cartella `api` e installa le dipendenze Python necessarie.

```bash
cd api
pip install -r requirements.txt
```

### 4. Inizializzare il database

Utilizzare lo script SQL presente nella cartella `database` per creare schema e tabelle.

File SQL: 
```text
database/schema.sql
```

### 5. Avviare l’API Flask

Avvia l’applicazione Flask dalla cartella `api`.

```bash
python app.py
```

L’API sarà disponibile all’indirizzo::
```
http://127.0.0.1:5000
```

### 6. Eseguire la pipeline ETL
Per eseguire il processo ETL e generare il dataset elaborato, accedi alla cartella etl e installa le dipendenze richieste:

```bash
cd etl
pip install -r requirements.txt
python pipeline/amazon_pipeline.py
```
---

## 🎯 Obiettivo del Progetto

L'obiettivo del progetto è di dimostrare la capacità di progettare e implementare una pipeline di data engineering end-to-end, applicando concetti fondamentali come:
- ingestione dei dati
- trasformazione e analisi statistica
- modellazione e interrogazione di database
- esposizione dei dati tramite API
- visualizzazione dei dati

---

## 🚀 Miglioramenti Futuri

- Automazione completa della fase di caricamento nel database  
- Containerizzazione tramite Docker  
- Controlli di qualità e validazione dei dati  
- Deploy dell’API su infrastruttura cloud  

---

## 👤 Autore

Francesco Saracino  
Junior Data Engineer


