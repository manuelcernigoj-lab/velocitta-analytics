CREATE TABLE stazioni (
    id_stazione     VARCHAR(20)     PRIMARY KEY,
    nome            VARCHAR(50)     NOT NULL,
    citta           VARCHAR(20)     NOT NULL,
    n_posti         INTEGER         NOT NULL,
    latitudine      FLOAT           NOT NULL,
    longitudine     FLOAT           NOT NULL
);

CREATE TABLE biciclette (
    id_bici             VARCHAR(10)     PRIMARY KEY,
    tipo                VARCHAR(20)     NOT NULL,
    citta               VARCHAR(20)     NOT NULL,
    stazione_corrente   VARCHAR(50)     NOT NULL,
    km_totali           FLOAT           NOT NULL DEFAULT 0
);

CREATE TABLE utenti (
    id_utente           VARCHAR(10)     PRIMARY KEY,
    nome                VARCHAR(50)     NOT NULL,
    citta               VARCHAR(20)     NOT NULL,
    tipo_abbonamento    VARCHAR(20)     NOT NULL,
    data_iscrizione     DATE            NOT NULL
);

CREATE TABLE corse (
    id_corsa            VARCHAR(10)     PRIMARY KEY,
    id_bici             VARCHAR(10)     NOT NULL REFERENCES biciclette(id_bici),
    id_utente           VARCHAR(10)     NOT NULL REFERENCES utenti(id_utente),
    stazione_partenza   VARCHAR(50)     NOT NULL,
    stazione_arrivo     VARCHAR(50)     NOT NULL,
    data_corsa          DATE            NOT NULL,
    durata_minuti       INTEGER         NOT NULL,
    km_percorsi         FLOAT           NOT NULL
);