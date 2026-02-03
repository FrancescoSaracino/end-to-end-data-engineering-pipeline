-- PostgreSQL initialization script for amazon_sales database
-- Converted from MySQL/MariaDB schema

-- Table structure for amazon_dataset_pulito
CREATE TABLE IF NOT EXISTS amazon_dataset_pulito (
    id SERIAL PRIMARY KEY,
    id_prodotto VARCHAR(255),
    nome_prodotto VARCHAR(500),
    categoria VARCHAR(255),
    prezzo_scontato DECIMAL(10,2),
    prezzo_originale DECIMAL(10,2),
    percentuale_sconto INTEGER,
    valutazione_media DECIMAL(3,2),
    conteggio_valutazioni INTEGER,
    descrizione_prodotto TEXT,
    id_utente VARCHAR(255),
    nome_utente VARCHAR(255),
    id_recensione VARCHAR(255),
    titolo_recensione VARCHAR(500),
    contenuto_recensione TEXT,
    link_immagine TEXT,
    link_prodotto TEXT
);

-- Create indexes for common queries
CREATE INDEX IF NOT EXISTS idx_id_prodotto ON amazon_dataset_pulito(id_prodotto);
CREATE INDEX IF NOT EXISTS idx_categoria ON amazon_dataset_pulito(categoria);
CREATE INDEX IF NOT EXISTS idx_valutazione ON amazon_dataset_pulito(valutazione_media);
