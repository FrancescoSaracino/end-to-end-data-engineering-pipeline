from abc import ABC
import pandas as pd
import os

# definizione di una classe astratta per la centralizzazione operazioni comuni
class ModelloBase(ABC):

    # metodo di inizializzazione
    def __init__(self, percorso_dataset, righe_da_saltare=0):
        self.dataframe = pd.read_csv(filepath_or_buffer=os.path.join(os.path.dirname(os.path.dirname(__file__)), percorso_dataset), skiprows=righe_da_saltare)

    # metodo per ottenimento informazioni generali
    @staticmethod
    def analisi_generali(df):
        print("------ Analisi Generali Dataframe ------")
        #print("Prime cinque osservazioni:", df.head().to_string(), sep="\n") # head() stampa le prime 5 osservazioni, per cambiare inserire valore tra ()
        #print("Ultime cinque osservazioni:", df.tail().to_string(), sep="\n") # tail() stampa le ultime 5 osservazioni, per cambiare come head()
        print("Informazioni generali dataframe:")
        df.info() # funzione per dati generali del dataframe

    @staticmethod
    # metodo per controllo valori univoci 
    def analisi_valori_univoci(df, variabili_da_droppare=None):
        print("------ Valori Univoci Dataframe ------")
        if variabili_da_droppare:
            df = df.drop(variabili_da_droppare, axis=1)
        for colonna in df.columns:
            print(f"In colonna {colonna} abbiamo {df[colonna].nunique()} valori univoci:")
            for valore in df[colonna].unique():
                print(valore)


    # metodo per analisi indici statistici delle variabili quantitative
    @staticmethod
    def analisi_indici_statistici(df):
        print("------ Indici Statistici Dataframe ------")
        indici_generali = df.describe()
        print("Indici statistici principali delle variabili quantitative", indici_generali.to_string(), sep="\n")
        # moda per variabili sia quantitative che categoriali
        for colonna in df.columns:
            print(f"Moda colonna {colonna}:", df[colonna].mode().iloc[0]) # iloc[0] ritorna il primo elemento della Series mode()

    # metodo per individuazione degli outliers nelle variabili quantitative
    @staticmethod 
    def individuazione_outliers(df, variabili_da_droppare=None):
        print("------ Individuazione Outliers Dataframe ------")
        if variabili_da_droppare:
            df = df.drop(variabili_da_droppare, axis=1)
        for colonna in df.columns:           
            # calcolo della differenza interquartile
            q1 = df[colonna].quantile(0.25)
            q3 = df[colonna].quantile(0.75)
            iqr = q3 - q1
            # calcolo limiti superiori/inferiori outliers
            limite_inferiore = q1 - 1.5 * iqr
            limite_superiore = q3 + 1.5 * iqr
            # individuazione effettiva outliers
            outliers = df[(df[colonna] < limite_inferiore) | (df[colonna] > limite_superiore)]
            print(f"Nella colonna {colonna} sono presenti n. {len(outliers)} outliers ({(len(outliers) / len(df)) * 100}%)") 

