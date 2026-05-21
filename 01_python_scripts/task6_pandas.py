"""
Task 6 — Pandas: Caricamento, Pulizia e Analisi

Contenuto:
    6.1 — Creazione DataFrame   : df_corse (80+ righe), df_bici (20+), df_utenti (25+)
    6.2 — Pulizia dati          : duplicati, NaN, datetime, colonne derivate
    6.3 — Apply e colonne       : tipo_corsa, velocita_media, costo_stimato
    6.4 — Aggregazioni e merge  : groupby, pivot, merge, top-N
"""

import pandas as pd
import numpy as np
from task1_utils import classifica_corsa


# --[creazione DataFrame]--

# [ 1 ] df_corse: 85 righe (80 base + 5 duplicati espliciti)
#                 presenti 8 NaN sparsi: 4 in durata_minuti, 4 in km_percorsi

corse_data = [
#    id_corsa id_bici   id_utente  citta      data_corsa     dur  km    fascia
    ("C-001", "MI-001", "U-MI-01", "Milano",  "2026-04-02",  22,  3.80, "mattina"),
    ("C-002", "MI-005", "U-MI-01", "Milano",  "2026-04-05",  35,  6.20, "mattina"),
    ("C-003", "MI-006", "U-MI-01", "Milano",  "2026-04-08",  18,  3.10, "pomeriggio"),
    ("C-004", "MI-001", "U-MI-01", "Milano",  "2026-04-10",  28,  4.90, "mattina"),
    ("C-005", "MI-007", "U-MI-02", "Milano",  "2026-04-12",  42,  7.50, "pomeriggio"),
    ("C-006", "MI-002", "U-MI-02", "Milano",  "2026-04-15",  15,  2.70, "sera"),
    ("C-007", "MI-008", "U-MI-03", "Milano",  "2026-04-18",  55,  9.80, "mattina"),
    ("C-008", "MI-003", "U-MI-03", "Milano",  "2026-04-20",  12,  2.10, "pomeriggio"),
    ("C-009", "MI-009", "U-MI-04", "Milano",  "2026-04-22",  33,  5.90, "sera"),
    ("C-010", "MI-005", "U-MI-04", "Milano",  "2026-04-25",  48,  8.60, "mattina"),
    ("C-011", "MI-001", "U-MI-05", "Milano",  "2026-05-02",  20,  3.50, "mattina"),
    ("C-012", "MI-006", "U-MI-05", "Milano",  "2026-05-08",  38,  6.80, "pomeriggio"),
    ("C-013", "MI-002", "U-MI-06", "Milano",  "2026-03-10",  25,  4.40, "sera"),
    ("C-014", "MI-007", "U-MI-06", "Milano",  "2026-03-15",  40,  7.10, "mattina"),
    ("C-015", "MI-003", "U-MI-07", "Milano",  "2026-03-20",  17,  3.00, "pomeriggio"),
    ("C-016", "MI-008", "U-MI-07", "Milano",  "2026-04-03",  52,  9.30, "sera"),
    ("C-017", "MI-004", "U-MI-08", "Milano",  "2026-04-07",  10,  1.80, "mattina"),
    ("C-018", "MI-009", "U-MI-08", "Milano",  "2026-04-11",  30,  5.40, "pomeriggio"),
    ("C-019", "MI-010", "U-MI-09", "Milano",  "2026-04-14",  45,  8.00, "sera"),
    ("C-020", "MI-001", "U-MI-09", "Milano",  "2026-04-17",  22,  3.90, "mattina"),
    # NaN su durata_minuti Milano
    ("C-021", "MI-005", "U-MI-10", "Milano",  "2026-04-21", None, 10.70, "pomeriggio"),
    ("C-022", "MI-006", "U-MI-10", "Milano",  "2026-04-24", None,  2.50, "sera"),
    # NaN su km_percorsi Milano
    ("C-023", "MI-007", "U-MI-01", "Milano",  "2026-05-05",  36,  None, "mattina"),
    ("C-024", "MI-002", "U-MI-02", "Milano",  "2026-04-04",  19,  None, "pomeriggio"),
    ("C-025", "MI-004", "U-MI-03", "Milano",  "2026-04-06",  27,  4.80, "sera"),
    ("C-026", "MI-008", "U-MI-04", "Milano",  "2026-04-09",   8,  1.40, "mattina"),
    ("C-027", "MI-003", "U-MI-05", "Milano",  "2026-04-13",  44,  7.90, "pomeriggio"),
    ("C-028", "MI-010", "U-MI-06", "Milano",  "2026-04-16",  31,  5.60, "sera"),
    # Roma
    ("C-029", "RM-001", "U-RM-01", "Roma",    "2026-04-01",  30,  5.40, "mattina"),
    ("C-030", "RM-005", "U-RM-01", "Roma",    "2026-04-04",  43,  7.70, "pomeriggio"),
    ("C-031", "RM-006", "U-RM-02", "Roma",    "2026-04-07",  19,  3.40, "sera"),
    ("C-032", "RM-002", "U-RM-02", "Roma",    "2026-04-10",  55,  9.90, "mattina"),
    ("C-033", "RM-007", "U-RM-03", "Roma",    "2026-04-13",  14,  2.50, "pomeriggio"),
    ("C-034", "RM-008", "U-RM-03", "Roma",    "2026-04-16",  38,  6.80, "sera"),
    ("C-035", "RM-003", "U-RM-04", "Roma",    "2026-04-19",  26,  4.70, "mattina"),
    ("C-036", "RM-009", "U-RM-04", "Roma",    "2026-04-22",  50,  8.90, "pomeriggio"),
    ("C-037", "RM-010", "U-RM-05", "Roma",    "2026-04-25",  22,  3.90, "sera"),
    ("C-038", "RM-004", "U-RM-05", "Roma",    "2026-04-28",  60, 10.80, "mattina"),
    ("C-039", "RM-005", "U-RM-06", "Roma",    "2026-05-04",  33,  5.90, "pomeriggio"),
    ("C-040", "RM-002", "U-RM-06", "Roma",    "2026-03-05",  28,  5.00, "sera"),
    ("C-041", "RM-006", "U-RM-07", "Roma",    "2026-03-12",  45,  8.10, "mattina"),
    ("C-042", "RM-007", "U-RM-07", "Roma",    "2026-03-19",  17,  3.00, "pomeriggio"),
    ("C-043", "RM-008", "U-RM-08", "Roma",    "2026-04-02",  52,  9.30, "sera"),
    ("C-044", "RM-003", "U-RM-08", "Roma",    "2026-04-06",  11,  2.00, "mattina"),
    # NaN su durata_minuti Roma
    ("C-045", "RM-009", "U-RM-09", "Roma",    "2026-04-10", None,  6.40, "pomeriggio"),
    ("C-046", "RM-010", "U-RM-09", "Roma",    "2026-04-14", None,  8.60, "sera"),
    # NaN su km_percorsi Roma
    ("C-047", "RM-004", "U-RM-10", "Roma",    "2026-04-18",  21,  None, "mattina"),
    ("C-048", "RM-005", "U-RM-10", "Roma",    "2026-04-22",  40,  None, "pomeriggio"),
    ("C-049", "RM-001", "U-RM-01", "Roma",    "2026-04-03",  24,  4.30, "sera"),
    ("C-050", "RM-003", "U-RM-02", "Roma",    "2026-04-08",  37,  6.60, "mattina"),
    # Torino
    ("C-051", "TO-001", "U-TO-01", "Torino",  "2026-04-01",  20,  3.60, "mattina"),
    ("C-052", "TO-005", "U-TO-01", "Torino",  "2026-04-04",  35,  6.30, "pomeriggio"),
    ("C-053", "TO-006", "U-TO-02", "Torino",  "2026-04-07",  48,  8.60, "sera"),
    ("C-054", "TO-002", "U-TO-02", "Torino",  "2026-04-10",  15,  2.70, "mattina"),
    ("C-055", "TO-007", "U-TO-03", "Torino",  "2026-04-13",  58, 10.40, "pomeriggio"),
    ("C-056", "TO-008", "U-TO-03", "Torino",  "2026-04-17",  26,  4.70, "sera"),
    ("C-057", "TO-003", "U-TO-04", "Torino",  "2026-04-21",  40,  7.20, "mattina"),
    ("C-058", "TO-009", "U-TO-04", "Torino",  "2026-04-25",  12,  2.10, "pomeriggio"),
    ("C-059", "TO-010", "U-TO-05", "Torino",  "2026-04-28",  33,  5.90, "sera"),
    ("C-060", "TO-004", "U-TO-05", "Torino",  "2026-05-05",  22,  3.90, "mattina"),
    ("C-061", "TO-002", "U-TO-06", "Torino",  "2026-03-08",  30,  5.40, "pomeriggio"),
    ("C-062", "TO-006", "U-TO-06", "Torino",  "2026-03-15",  55,  9.90, "sera"),
    ("C-063", "TO-007", "U-TO-07", "Torino",  "2026-03-22",  18,  3.20, "mattina"),
    ("C-064", "TO-008", "U-TO-07", "Torino",  "2026-04-03",  42,  7.50, "pomeriggio"),
    ("C-065", "TO-009", "U-TO-08", "Torino",  "2026-04-09",  10,  1.80, "sera"),
    ("C-066", "TO-010", "U-TO-08", "Torino",  "2026-04-13",  37,  6.60, "mattina"),
    ("C-067", "TO-001", "U-TO-09", "Torino",  "2026-04-17",  50,  8.90, "pomeriggio"),
    ("C-068", "TO-005", "U-TO-09", "Torino",  "2026-04-21",  24,  4.30, "sera"),
    ("C-069", "TO-003", "U-TO-10", "Torino",  "2026-04-25",  44,  7.90, "mattina"),
    ("C-070", "TO-006", "U-TO-10", "Torino",  "2026-04-29",  16,  2.90, "pomeriggio"),
    ("C-071", "TO-001", "U-TO-01", "Torino",  "2026-04-05",  28,  5.00, "sera"),
    ("C-072", "TO-004", "U-TO-02", "Torino",  "2026-04-09",  39,  7.00, "mattina"),
    ("C-073", "TO-008", "U-TO-03", "Torino",  "2026-04-12",   8,  1.40, "pomeriggio"),
    ("C-074", "TO-003", "U-TO-04", "Torino",  "2026-04-16",  46,  8.30, "sera"),
    ("C-075", "TO-009", "U-TO-05", "Torino",  "2026-04-20",  21,  3.80, "mattina"),
    ("C-076", "MI-005", "U-MI-07", "Milano",  "2026-04-05",  32,  5.70, "pomeriggio"),
    ("C-077", "MI-004", "U-MI-08", "Milano",  "2026-04-09",  46,  8.20, "sera"),
    ("C-078", "MI-010", "U-MI-09", "Milano",  "2026-04-12",  21,  3.70, "mattina"),
    ("C-079", "RM-001", "U-RM-03", "Roma",    "2026-04-15",  18,  3.20, "pomeriggio"),
    ("C-080", "RM-010", "U-RM-04", "Roma",    "2026-04-20",  53,  9.50, "sera"),
]

# -- 5 righe duplicate aggiunte in fondo (stessa id_corsa e stessi dati)
duplicati = [
    ("C-001", "MI-001", "U-MI-01", "Milano",  "2026-04-02",  22,  3.80, "mattina"),
    ("C-015", "MI-003", "U-MI-07", "Milano",  "2026-03-20",  17,  3.00, "pomeriggio"),
    ("C-029", "RM-001", "U-RM-01", "Roma",    "2026-04-01",  30,  5.40, "mattina"),
    ("C-051", "TO-001", "U-TO-01", "Torino",  "2026-04-01",  20,  3.60, "mattina"),
    ("C-062", "TO-006", "U-TO-06", "Torino",  "2026-03-15",  55,  9.90, "sera"),
]

colonne_corse = ["id_corsa", "id_bici", "id_utente", "citta",
                 "data_corsa", "durata_minuti", "km_percorsi", "fascia_oraria"]

df_corse = pd.DataFrame(corse_data + duplicati, columns = colonne_corse)


# [ 2 ] df_bici: 20 righe
bici_data = [
#    id_bici   tipo         citta      anno  costo
    ("MI-001", "classica",  "Milano",  2021, 320.00),
    ("MI-002", "classica",  "Milano",  2020, 290.00),
    ("MI-003", "classica",  "Milano",  2022, 310.00),
    ("MI-004", "classica",  "Milano",  2021, 305.00),
    ("MI-005", "elettrica", "Milano",  2023, 850.00),
    ("MI-006", "elettrica", "Milano",  2022, 820.00),
    ("MI-007", "elettrica", "Milano",  2023, 870.00),
    ("RM-001", "classica",  "Roma",    2020, 280.00),
    ("RM-002", "classica",  "Roma",    2021, 295.00),
    ("RM-003", "classica",  "Roma",    2022, 315.00),
    ("RM-005", "elettrica", "Roma",    2023, 860.00),
    ("RM-006", "elettrica", "Roma",    2022, 830.00),
    ("RM-007", "elettrica", "Roma",    2023, 845.00),
    ("TO-001", "classica",  "Torino",  2021, 300.00),
    ("TO-002", "classica",  "Torino",  2020, 275.00),
    ("TO-003", "classica",  "Torino",  2022, 320.00),
    ("TO-004", "classica",  "Torino",  2021, 290.00),
    ("TO-005", "elettrica", "Torino",  2023, 840.00),
    ("TO-006", "elettrica", "Torino",  2022, 815.00),
    ("TO-008", "elettrica", "Torino",  2023, 855.00),
]

colonne_bici = ["id_bici", "tipo", "citta", "anno_acquisto", "costo_acquisto"]
df_bici = pd.DataFrame(bici_data, columns = colonne_bici)


# [ 3 ] df_utenti: 25 righe
utenti_data = [
#    id_utente  nome                citta      abbonamento  iscrizione
    ("U-MI-01", "Luca Rossi",       "Milano",  "Premium",   "2024-01-10"),
    ("U-MI-02", "Sara Bianchi",     "Milano",  "Base",      "2024-03-22"),
    ("U-MI-03", "Marco Verdi",      "Milano",  "Premium",   "2023-11-05"),
    ("U-MI-04", "Anna Neri",        "Milano",  "Base",      "2024-06-18"),
    ("U-MI-05", "Paolo Ferrari",    "Milano",  "Premium",   "2023-08-30"),
    ("U-MI-06", "Giulia Russo",     "Milano",  "Base",      "2024-02-14"),
    ("U-MI-07", "Matteo Esposito",  "Milano",  "Premium",   "2023-12-01"),
    ("U-MI-08", "Chiara Romano",    "Milano",  "Base",      "2024-04-09"),
    ("U-MI-09", "Davide Greco",     "Milano",  "Premium",   "2024-01-25"),
    ("U-MI-10", "Elena Marino",     "Milano",  "Base",      "2024-05-03"),
    ("U-RM-01", "Alessio Conti",    "Roma",    "Premium",   "2023-09-12"),
    ("U-RM-02", "Francesca Ricci",  "Roma",    "Base",      "2024-07-01"),
    ("U-RM-03", "Simone Lombardi",  "Roma",    "Premium",   "2023-10-20"),
    ("U-RM-04", "Valentina Costa",  "Roma",    "Base",      "2024-02-28"),
    ("U-RM-05", "Roberto Gallo",    "Roma",    "Premium",   "2023-07-15"),
    ("U-RM-06", "Monica Bruno",     "Roma",    "Base",      "2024-08-05"),
    ("U-RM-07", "Stefano Martini",  "Roma",    "Premium",   "2024-03-11"),
    ("U-RM-08", "Laura Serra",      "Roma",    "Base",      "2024-01-30"),
    ("U-RM-09", "Andrea Fontana",   "Roma",    "Premium",   "2023-11-22"),
    ("U-RM-10", "Paola Caruso",     "Roma",    "Base",      "2024-06-07"),
    ("U-TO-01", "Giorgio Fiore",    "Torino",  "Premium",   "2023-12-15"),
    ("U-TO-02", "Silvia Marini",    "Torino",  "Base",      "2024-04-20"),
    ("U-TO-03", "Fabio Santoro",    "Torino",  "Premium",   "2024-02-08"),
    ("U-TO-04", "Cristina Vitale",  "Torino",  "Base",      "2024-07-14"),
    ("U-TO-05", "Enrico De Luca",   "Torino",  "Premium",   "2023-08-03"),
    ("U-TO-06", "Marta Galli",      "Torino",  "Base",      "2024-05-25"),
    ("U-TO-07", "Nicola Ferri",     "Torino",  "Premium",   "2023-10-10"),
    ("U-TO-08", "Teresa Monti",     "Torino",  "Base",      "2024-03-17"),
    ("U-TO-09", "Claudio Barbieri", "Torino",  "Premium",   "2024-01-05"),
    ("U-TO-10", "Irene Cattaneo",   "Torino",  "Base",      "2024-06-30"),
]

colonne_utenti = ["id_utente", "nome", "citta", "tipo_abbonamento", "data_iscrizione"]
df_utenti = pd.DataFrame(utenti_data, columns = colonne_utenti)


# --[pulizia dati]--
print(f"\n[ 6.2 ] — Pulizia dati")

print("\n• PRIMA DELLA PULIZIA\n")
print("\n", df_corse.info())
print("\n", df_corse.describe())

print("\n• PULIZIA ...")
# --[rimozione duplicati]--
n_prima = len(df_corse)
df_corse = df_corse.drop_duplicates()
print(f"\n • Righe duplicate rimosse: {n_prima - len(df_corse)} ...")

# --[durata_minuti NaN → mediana per città]--
mediana_per_citta = df_corse.groupby("citta")["durata_minuti"].transform("median")
# ↘ groupby + transform calcola la mediana per città e la propaga su ogni riga
df_corse["durata_minuti"] = df_corse["durata_minuti"].fillna(mediana_per_citta)
# ↘ fillna sostituisce solo i NaN con il valore della mediana corrispondente alla città
print(" • Valori NaN in durata_minuti rimpiazzati con mediana per città ...")

# --[km_percorsi NaN → durata_minuti * 0.18]--
df_corse["km_percorsi"] = df_corse["km_percorsi"].fillna(df_corse["durata_minuti"] * 0.18)
# ↘ stima i km percorsi in base alla durata della corsa
print(" • Valori NaN in km_percorsi rimpiazzati con stima (durata_minuti * 0.18) ...")

# --[conversione data_corsa da stringa a datetime]--
df_corse["data_corsa"] = pd.to_datetime(df_corse["data_corsa"])
print(" • Conversione data_corsa da stringa a datetime ...")

# --[colonne derivate da data_corsa]--
df_corse["mese"] = df_corse["data_corsa"].dt.month
print(" • Aggiunta colonna 'mese' (int) ...")

giorni_ita = {
    "Monday":    "Lunedì",
    "Tuesday":   "Martedì",
    "Wednesday": "Mercoledì",
    "Thursday":  "Giovedì",
    "Friday":    "Venerdì",
    "Saturday":  "Sabato",
    "Sunday":    "Domenica"
    }
# ↘ dt.day_name() restituisce il nome del giorno in inglese → mappa in italiano
df_corse["giorno_settimana"] = df_corse["data_corsa"].dt.day_name().map(giorni_ita)
print(" • Aggiunta colonna 'giorno_settimana' (es. Lunedì).")

print("\n• DOPO LA PULIZIA\n")
print("\n", df_corse.info())
print("\n", df_corse.describe())


# --[apply e colonne derivate]--
print(f"\n[ 6.3 ] — Apply e colonne derivate")

# --[tipo_corsa: applica classifica_corsa() importata da task1_utils]--
df_corse["tipo_corsa"] = df_corse["durata_minuti"].apply(classifica_corsa)

# --[velocita_media in km/h]--
df_corse["velocita_media"] = df_corse["km_percorsi"] / (df_corse["durata_minuti"] / 60).round(2)

# --[costo_stimato con logica a scaglioni ─────────────────────────────────────
def calcola_costo(durata: float) -> float:
    """
    Calcola il costo stimato di una corsa in base alla durata in minuti.
    Tariffe:
        breve (< 15 min)    : € 1.50 fisso
        media (15-45 min)   : € 2.50 + € 0.10 x (minuti - 15)
        lunga (> 45 min)    : € 5.00 + € 0.08 x (minuti - 45)
    """
    if durata < 15:
        return 1.50
    elif durata <= 45:
        return round(2.50 + 0.10 * (durata - 15), 2)
    else:
        return round(5.00 + 0.08 * (durata - 45), 2)

df_corse["costo_stimato"] = df_corse["durata_minuti"].apply(calcola_costo)

print("\n• AGGIUNTE COLONNE: 'tipo_corsa' | 'velocita_media' | 'costo_stimato'")
print("\n• Prime 10 righe con colonne aggiunte:")
print(df_corse.head(10))

# --[aggregazioni e merge]--
print(f"\n[ 6.4 ] — Aggregazioni e merge")

# --[groupby per città]--
agg_citta = df_corse.groupby("citta").agg(
    n_corse      = ("id_corsa",      "count"),
    durata_media = ("durata_minuti", "mean"),
    km_totali    = ("km_percorsi",   "sum"),
    costo_totale = ("costo_stimato", "sum")
).round(2)

print("\n• Statistiche per città:")
print(agg_citta)

# --[groupby per fascia_oraria]--
agg_fascia = df_corse.groupby("fascia_oraria").agg(
    n_corse        = ("id_corsa",       "count"),
    velocita_media = ("velocita_media", "mean")
).round(2)

print("\n• Statistiche per fascia oraria:")
print(agg_fascia)

# --[pivot table: città x tipo_corsa]--
pivot = pd.pivot_table(
    df_corse,
    index   = "citta",
    columns = "tipo_corsa",
    values  = "id_corsa",
    aggfunc = "count",      # aggfunc = "count" conta le corse
    fill_value = 0          # fill_value = 0 sostituisce NaN con 0
)

print("\n• Pivot - corse per città e tipo:")
print(pivot)

# --[merge: df_corse + df_bici + df_utenti]--
df_merged = (
    df_corse
    .merge(df_bici,    on = "id_bici",    how = "left")
    .merge(df_utenti,  on = "id_utente",  how = "left")
    # ↘ left join: mantiene tutte le corse anche se la bici o l'utente non sono
    #   presenti in df_bici / df_utenti (es. bici non censite nel dataset)
    )

print("\n• Merge - prime 5 righe:")
print(df_merged.head())
print(f"\n• Colonne disponibili ({len(df_merged.columns)}):")
print(list(df_merged.columns))

# --[top-N]--

# top 5 biciclette per numero di corse
top5_bici = (
    df_corse
    .groupby("id_bici")["id_corsa"]
    .count()
    .sort_values(ascending = False)
    .head(5)
    .reset_index()                              # riporta id_bici da indice a colonna
    .rename(columns = {"id_corsa": "n_corse"})  # rinomina dopo reset_index
    )
print("\n• Top 5 biciclette per corse:")
print(top5_bici)

# top 3 utenti Premium per costo totale
top3_premium = (
    df_merged[df_merged["tipo_abbonamento"] == "Premium"]
    .groupby(["id_utente", "nome"])["costo_stimato"]
    .sum()
    .sort_values(ascending = False)
    .head(3)
    .reset_index()                             
    .rename(columns = {"costo_stimato": "costo_totale"})
    .round(2)
    )
print("\n• Top 3 utenti Premium per costo totale:")
print(top3_premium.to_string())

# statistica extra → città con velocità media più alta
print("\n• Velocità media per città:")
print(
    df_corse.groupby("citta")["velocita_media"]
    .mean()
    .round(2)
    .sort_values(ascending = False)
    .reset_index()
    )

# statistica extra → distribuzione abbonamenti per città
print("\n• Distribuzione abbonamenti per città:")
print(
    df_merged.groupby(["citta", "tipo_abbonamento"])["id_corsa"]
    .count()
    .unstack(fill_value = 0)    # disimpila i dati costruendo un formato pivot
    )