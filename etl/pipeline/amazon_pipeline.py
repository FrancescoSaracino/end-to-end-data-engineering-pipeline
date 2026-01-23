from base_pipeline import ModelloBase
import pandas as pd
from scipy.stats import chi2_contingency, contingency, spearmanr, f_oneway
import matplotlib.pyplot as plt
import seaborn as sns
import os


class ModelloAmazon(ModelloBase):
    def __init__(self, percorso_dataset, righe_da_saltare=0,percorso_dataset_sistemato="../dataset/processed/processed_data.csv"):
        super().__init__(percorso_dataset, righe_da_saltare)

        self.percorso_dataset_sistemato = percorso_dataset_sistemato

        # Creazione dataset sistemato se non esiste
        dataset_dir = os.path.dirname(self.percorso_dataset_sistemato)
        if dataset_dir and not os.path.exists(dataset_dir):
            os.makedirs(dataset_dir)

        if os.path.exists(self.percorso_dataset_sistemato):
            self.dataframe_sistemato = pd.read_csv(self.percorso_dataset_sistemato)
        else:
            self.dataframe_sistemato = self.sistemazione_dataframe()
            self.dataframe_sistemato.to_csv(self.percorso_dataset_sistemato, index=False)

    def sistemazione_dataframe(self):
        dataframe_sistemato = (self.dataframe.drop_duplicates(subset="product_id", keep='first').copy())

        dataframe_sistemato.loc[:, 'category'] = (dataframe_sistemato['category'].str.split('|').str[0])

        dataframe_sistemato = dataframe_sistemato.dropna(subset=['rating_count'])

        dataframe_sistemato.loc[:, 'rating'] = (dataframe_sistemato['rating'].str.rstrip('|'))
        dataframe_sistemato = dataframe_sistemato[dataframe_sistemato['rating'] != '']
        dataframe_sistemato = dataframe_sistemato.dropna(subset=['rating'])

        dataframe_sistemato.loc[:, 'rating_count'] = (dataframe_sistemato['rating_count'].str.replace(',', ''))

        # rinominazione colonne in italiano
        dataframe_sistemato = dataframe_sistemato.rename(columns={
            "product_id": "id_prodotto",
            'rating_count': "conteggio_valutazioni",
            'rating': "valutazione_media",
            'category': 'categoria',
            'product_name': "nome_prodotto",
            'discounted_price': "prezzo_scontato",
            'actual_price': "prezzo_originale",
            'about_product': "descrizione_prodotto",
            'user_id': "id_utente",
            'user_name': "nome_utente",
            'review_id': "id_recensione",
            'review_title': "titolo_recensione",
            'review_content': "contenuto_recensione",
            'img_link': "link_immagine",
            'product_link': "link_prodotto",
            'discount_percentage': 'percentuale_sconto'
        })

        # cambiamento tipo dato object a int, float, str
        dataframe_sistemato.loc[:, 'percentuale_sconto'] = (dataframe_sistemato['percentuale_sconto'].str.rstrip('%').astype(int))
        dataframe_sistemato.loc[:, 'valutazione_media'] = (dataframe_sistemato['valutazione_media'].astype(float))
        dataframe_sistemato.loc[:, 'conteggio_valutazioni'] = (dataframe_sistemato['conteggio_valutazioni'].astype(int))
        dataframe_sistemato.loc[:, 'categoria'] = (dataframe_sistemato['categoria'].astype(str))
        dataframe_sistemato.loc[:, 'id_prodotto'] = (dataframe_sistemato['id_prodotto'].astype(str))

        # rimozione simbolo rupee da discounted_price e actual_price e cambio valuta in euro
        dataframe_sistemato['prezzo_scontato'] = (dataframe_sistemato['prezzo_scontato'].str.replace('₹', '', regex=False).str.replace(',', ''))   
        dataframe_sistemato['prezzo_originale'] = (dataframe_sistemato['prezzo_originale'].str.replace('₹', '', regex=False).str.replace(',', ''))

        # cambiamento tipo dato object a float per discounted_price e actual_price e arrotondamento a 2 decimali
        dataframe_sistemato['prezzo_scontato'] = (dataframe_sistemato['prezzo_scontato'].astype(float) * 0.011).round(2) 
        dataframe_sistemato['prezzo_originale'] = (dataframe_sistemato['prezzo_originale'].astype(float) * 0.011).round(2)
        return dataframe_sistemato

    def analisi_anova(self, dataframe):
        categorie = dataframe['categoria'].value_counts()
        categorie_valide = categorie[categorie >= 20].index

        dataframe_filtrato = dataframe[dataframe['categoria'].isin(categorie_valide)]

        gruppi = [dataframe_filtrato[dataframe_filtrato['categoria'] == categoria]['valutazione_media']for categoria in categorie_valide]

        f_stat, p_value = f_oneway(*gruppi)

        print("Risultati ANOVA:")
        print(f"F-statistic: {f_stat}")
        print(f"p-value: {p_value}")

        if p_value < 0.05:
            print("Il risultato dell'analisi one-way anova è statisticamente rilevente perchè p-value < 0.05, per cui si respinge l'ipotesi nulla")
            if f_stat > 10:
                print("il valore F-statistic del metodo Anova one-way ci indica che l'impatto della categoria sul rating è > 10, cioè che esiste una differenza forte tra le medie delle valutazioni delle diverse categorie.")   
            elif f_stat >=2 and f_stat <=10:
                print("il valore F-statistic del metodo Anova one-way ci indica che l'impatto della categoria sul rating è >=2 e <=10, cioè che esiste una differenza moderata tra le medie delle valutazioni delle diverse categorie.") 
            elif f_stat < 2:
                print("il valore F-statistic del metodo Anova one-way ci indica che l'impatto della categoria sul rating è < 2, cioè che c'è una differenza debole tra le medie delle valutazioni delle diverse categorie.")    
        else:
            print("Il risultato dell'analisi one-way anova non è statisticamente rilevente perchè p-value > 0.05, per cui si accetta l'ipotesi nulla")

    def analisi_spearman(self, dataframe):
        corr, p_value = spearmanr(
            dataframe['percentuale_sconto'],
            dataframe['conteggio_valutazioni']
        )

        print("Risultati Spearman:")
        print(f"Coefficiente di correlazione: {corr}")
        print(f"p-value: {p_value}")

        if p_value < 0.05:
            print("Il coefficiente di correlazione è statisticamente significativo.")
            if corr > -0.3 and corr < 0.3:
                forza = "debole perchè vicina a 0"
            elif (corr >= 0.3 and corr < 0.7) or (corr <= -0.3 and corr > -0.7):
                forza = "media perchè tra 0.3 e 0.7"
            else:
                forza = "forte perchè oltre 0.7"
            print(f"La correlazione è {forza}.")
        else:
            print("Non c'è una correlazione significativa tra percentuale di sconto e valutazione media.")

        

    def boxplot_valutazioni_per_categoria(self, dataframe):
        plt.figure(figsize=(12, 6))
        sns.boxplot(x='categoria', y='valutazione_media', data=dataframe)
        plt.xticks(rotation=25)
        plt.title('Distribuzione delle Valutazioni Medie per Categoria')
        plt.xlabel('Categoria', labelpad=-5)
        plt.ylabel('Valutazione Media')
        plt.tight_layout()
        plt.show()

    def scatterplot_sconto_vs_valutazione(self, dataframe):
        plt.figure(figsize=(10, 6))
        sns.scatterplot(
            x='percentuale_sconto',
            y='conteggio_valutazioni',
            data=dataframe
        )
        plt.title('Percentuale di Sconto vs Conteggio Valutazioni')
        plt.xlabel('Percentuale di Sconto')
        plt.ylabel('Conteggio valutazioni')
        plt.tight_layout()
        plt.show()
        return plt


# utilizzo modello
modello = ModelloAmazon(percorso_dataset="../dataset/raw/raw_data.csv")
modello.analisi_generali(modello.dataframe_sistemato)
# modello.analisi_valori_univoci(modello.dataframe_sistemato)
modello.individuazione_outliers(modello.dataframe_sistemato, variabili_da_droppare=["id_prodotto", "categoria","nome_prodotto", "prezzo_scontato", "prezzo_originale", "id_utente", "nome_utente", "id_recensione", "titolo_recensione", "contenuto_recensione", "link_immagine", "link_prodotto", "descrizione_prodotto"])

# analisi statistiche
modello.analisi_anova(modello.dataframe_sistemato)
modello.analisi_spearman(modello.dataframe_sistemato)

# grafici
modello.boxplot_valutazioni_per_categoria(modello.dataframe_sistemato)
modello.scatterplot_sconto_vs_valutazione(modello.dataframe_sistemato)


