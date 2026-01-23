from cerberus import Validator


class Amazon:


    def __init__(
        self,id = None,
        id_prodotto=None,
        nome_prodotto=None,
        categoria=None,
        prezzo_scontato=None,
        prezzo_originale=None,
        percentuale_sconto=None,
        valutazione_media=None,
        conteggio_valutazioni=None,
        descrizione_prodotto=None,
        id_utente=None,
        nome_utente=None,
        id_recensione=None,
        titolo_recensione=None,
        contenuto_recensione=None,
        link_immagine=None,
        link_prodotto=None
 ):
        self.id = id
        self.id_prodotto = id_prodotto
        self.nome_prodotto = nome_prodotto
        self.categoria = categoria
        self.prezzo_scontato = prezzo_scontato
        self.prezzo_originale = prezzo_originale
        self.percentuale_sconto = percentuale_sconto
        self.valutazione_media = valutazione_media
        self.conteggio_valutazioni = conteggio_valutazioni
        self.descrizione_prodotto = descrizione_prodotto
        self.id_utente = id_utente
        self.nome_utente = nome_utente
        self.id_recensione = id_recensione
        self.titolo_recensione = titolo_recensione
        self.contenuto_recensione = contenuto_recensione
        self.link_immagine = link_immagine
        self.link_prodotto = link_prodotto



    def serializzazione_amazon(self):
        return {
            "id": self.id,
            "id_prodotto": self.id_prodotto,
            "nome_prodotto": self.nome_prodotto,
            "categoria": self.categoria,
            "prezzo_scontato": self.prezzo_scontato,
            "prezzo_originale": self.prezzo_originale,
            "percentuale_sconto": self.percentuale_sconto,
            "valutazione_media": self.valutazione_media,
            "conteggio_valutazioni": self.conteggio_valutazioni,
            "descrizione_prodotto": self.descrizione_prodotto,
            "id_utente": self.id_utente,
            "nome_utente": self.nome_utente,
            "id_recensione": self.id_recensione,
            "titolo_recensione": self.titolo_recensione,
            "contenuto_recensione": self.contenuto_recensione,
            "link_immagine": self.link_immagine,
            "link_prodotto": self.link_prodotto
        }   



        

