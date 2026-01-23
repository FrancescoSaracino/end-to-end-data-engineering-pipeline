# service/amazon_service.py
from model.amazon import Amazon
from repository.repository import Repository

class AmazonService:
    def __init__(self):
        self.repository = Repository()

    def elenco_prodotti_amazon(self):
        sql = "SELECT * FROM amazon_dataset_pulito"
        ottenuto_db = self.repository.recupero_multiplo(sql)

        if isinstance(ottenuto_db, str):
            # Restituisci array vuoto invece di oggetto per JS
            return [], 500

        # Trasforma in lista di dizionari
        prodotti = [Amazon(*record).serializzazione_amazon() for record in ottenuto_db]

        return prodotti, 200


    # Metodo per ottenere un singolo prodotto tramite id_prodotto (alfanumerico)
    def dati_prodotto(self, id_prodotto):
        id_prodotto = id_prodotto.strip()  # rimuove spazi accidentali

        # Query case-insensitive per ID alfanumerico
        sql = "SELECT * FROM amazon_dataset_pulito WHERE LOWER(id_prodotto) = LOWER(%s)"
        valori = (id_prodotto,)
        ottenuto_db = self.repository.recupero_singolo(sql, valori)

        if isinstance(ottenuto_db, str):
            return {"codice": 500, "messaggio": ottenuto_db}, 500
        elif not ottenuto_db:
            return {"codice": 404, "messaggio": "prodotto non trovato"}, 404

        return Amazon(*ottenuto_db).serializzazione_amazon(), 200
