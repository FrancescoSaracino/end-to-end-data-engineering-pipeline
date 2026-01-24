[English](README.md) | [Italiano](README.it.md)

# End-to-End Data Engineering Pipeline

## 📌 Overview

This project was developed as part of an intensive **Junior Data Engineer training program** and serves as a practical implementation of an **end-to-end data pipeline**.

The goal is to design and implement a complete data workflow covering the entire data lifecycle: from data ingestion and transformation, to API exposure and data visualization.

The project is intended as a hands-on demonstration of core **data engineering concepts**, data integration, and analytical processing.

---

## 🏗️ Project Architecture

The pipeline follows these main steps:

1. Ingestion of a raw dataset in CSV format  
2. Data transformation and analysis using Python  
3. Generation of a processed dataset  
4. Data loading into a relational database  
5. Data exposure through REST APIs  
6. Data visualization using Power BI  

---

## 🔄 Data Ingestion & ETL

The first phase of the project uses a **public dataset in CSV format** (`raw_data.csv`), stored locally in the project directory.

Using **Python** and an **object-oriented programming** approach, the raw dataset is cleaned, transformed, and analyzed.  
The following libraries were used:

- **pandas** for data manipulation and transformation  
- **scipy** for statistical analysis  
- **matplotlib** and **seaborn** for exploratory data visualization  

Main activities include:
- data cleaning  
- data transformations (e.g. data type conversion)  
- exploratory data analysis  

At the end of the extraction and transformation process, a new CSV file named **`processed_data.csv`** is generated.

> **Note:** the loading of the processed dataset into the database is currently performed manually.  
> For this reason, the pipeline can be considered **semi-automated**, with a focus on data transformation and analysis.

---

## 📊 Statistical Analysis

Several **descriptive statistical indicators** were computed on the processed dataset, and **outliers** were identified for quantitative variables.

Additionally, the following analyses were performed:
- **One-Way ANOVA**
- **Spearman correlation**

to investigate relationships between selected variables in the dataset.

---

## 🗄️ Database & REST API

The **`processed_data.csv`** file was imported into a **MySQL database** using **phpMyAdmin in a local XAMPP environment**.

Based on this database, a **REST API** was developed using **Flask (Python)**.  
The API exposes multiple **GET endpoints** that query the database and return results in **JSON format**.

Database configuration is managed through **environment variables (`.env`)**. Sensitive information is excluded from version control, following common backend best practices.

One of the endpoints also includes a **simple frontend interface** for data exploration.

---

## 📈 Data Visualization

Finally, starting from the **`processed_data.csv`** file, a **Power BI dashboard** was created to visualize the main insights of the dataset through charts and indicators.

---

## 📂 Project Structure

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
├── etl/                 # ETL & statistical analysis
│   ├── requirements.txt
│   └── pipeline/
│       ├── base_pipeline.py        # base pipeline class
│       └── amazon_pipeline.py     # specific pipeline (entry point)
├── bi/
│   └── dashboard.pbix              # Power BI dashboard
└── database/
    └── schema.sql
```
---

## ▶️ How to Run the Project (Local Setup)

### Prerequisites
- Python 3.9 or higher  
- MySQL installed and running locally  
- Virtual environment (recommended)  

### 1. Clone the repository
Clone the project repository and move into the project root directory.

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Set up environment variables

Inside the `api` folder, create a `.env` file using the provided example file.

```bash
cp api/.env.example api/.env
```

Edit the `.env` file if necessary (for example, database name, user, or port).

### 3. Install API dependencies

Move into the `api` folder and install the required Python dependencies.

```bash
cd api
pip install -r requirements.txt
```

### 4. Initialize the database

Use the SQL script located in the `database` folder to create the database schema and tables in your local MySQL instance.

SQL file:
```text
database/schema.sql
```

### 5. Run the Flask API

Start the Flask application from the `api` folder.

```bash
python app.py
```

Once the application is running, the API will be available at:
```
http://127.0.0.1:5000
```

### 6. Run the ETL pipeline
To execute the ETL process and generate the processed dataset, move into the `etl` folder and install the required dependencies:

```bash
cd etl
pip install -r requirements.txt
python pipeline/amazon_pipeline.py
```
---

## 🎯 Purpose

The purpose of this project is to demonstrate the ability to design and implement an **end-to-end data pipeline**, applying fundamental data engineering concepts such as:
- data ingestion  
- data transformation  
- statistical analysis  
- database modeling and querying  
- API-based data exposure  
- data visualization  

---

## 🚀 Future Improvements

- Fully automate the data loading phase into the database  
- Containerize the application using Docker  
- Add data quality checks and validation  
- Deploy the API on cloud infrastructure  

---

## 👤 Author

Francesco Saracino  
Junior Data Engineer


