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
import random
from task1_utils import classifica_corsa


# --[creazione DataFrame]--

# [ 1 ] df_corse: 185 righe (180 base + 5 duplicati espliciti)
#                 presenti 8 NaN sparsi: 4 in durata_minuti, 4 in km_percorsi
random.seed(42)
np.random.seed(42)

# --[configurazioni base]--
citta_list = ["Milano", "Roma", "Torino"]
date_list = pd.date_range(
    start = "2026-05-01",
    end   = "2026-05-15",
    freq  = "D")
fasce = ["mattina", "pomeriggio", "sera"]

# giorni con picchi realistici:
giorni_picco = {
    "Monday":    1.7,
    "Tuesday":   1.8,
    "Wednesday": 1.9,
    "Thursday":  1.8,
    "Friday":    1.6,
    # ↘ lunedì/venerdì: commuting
    "Saturday":  1.0,
    "Sunday":    0.8}
    # ↘ weekend: utilizzo leisure

# distribuzione fasce orarie
fascia_weights_weekday = [
    0.45,  # mattina        -> commuting
    0.20,  # pomeriggio     -> uso normale
    0.35]  # sera           -> svago / rientro
fascia_weights_weekend = [
    0.20,  # mattina
    0.35,  # pomeriggio
    0.45]  # sera

records = []
id_counter = 1

# --[generazione dati]--
for data in date_list:
    giorno_nome = data.day_name()

    # corse base giornaliere
    corse_giornaliere = 8

    # applicazione picchi
    moltiplicatore = giorni_picco.get(giorno_nome, 1)
    corse_giornaliere = int(corse_giornaliere * moltiplicatore)

    # rumore realistico
    corse_giornaliere += np.random.randint(low = 0, high = 2)
    for _ in range(corse_giornaliere):
        # lista delle città con pesi differenti
        citta = random.choices(
            citta_list,
            weights = [0.45, 0.35, 0.20])[0]

        # sigle delle città per id_bici
        sigla = {
            "Milano":   "MI",
            "Roma":     "RM",
            "Torino":   "TO"
            }[citta]

        # distribuzione fasce diversa weekend/feriali
        if giorno_nome in ["Saturday", "Sunday"]:
            fascia = random.choices(
                population = fasce,
                weights = fascia_weights_weekend)[0]
        else:
            fascia = random.choices(
                population = fasce,
                weights = fascia_weights_weekday)[0]

        # durate realistiche per fascia
        if fascia == "mattina":
            durata = np.random.randint(low = 8, high = 30)
            km = round(np.random.uniform(low = 1.5, high = 6.0), 2)
        elif fascia == "pomeriggio":
            durata = np.random.randint(low = 15, high = 45)
            km = round(np.random.uniform(low = 2.0, high = 10.0), 2)
        else:
            durata = np.random.randint(low = 20, high = 60)
            km = round(np.random.uniform(low = 3.0, high = 15.0), 2)

        record = {
            "id_corsa": f"C-{id_counter:03d}",
            "id_bici": f"{sigla}-{np.random.randint(1, 41):03d}",
            "id_utente": f"U-{sigla}-{np.random.randint(1, 81):02d}",
            "citta": citta,
            "data_corsa": data.strftime("%Y-%m-%d"),
            "durata_minuti": durata,
            "km_percorsi": km,
            "fascia_oraria": fascia}

        records.append(record)
        id_counter += 1

# --[creazione DataFrame]--
df_corse = pd.DataFrame(records)

# --[inserimento 5 duplicati]--
duplicati = df_corse.sample(n = 5, random_state = 42)
df_corse = pd.concat([df_corse, duplicati], ignore_index = True)

# --[inserimento 8 NaN]--
nan_idx_durata = np.random.choice(df_corse.index, size = 4, replace = False)
nan_idx_km = np.random.choice(df_corse.index, size = 4, replace = False)

df_corse.loc[nan_idx_durata, "durata_minuti"] = np.nan
df_corse.loc[nan_idx_km, "km_percorsi"] = np.nan

# [ 2 ] df_bici: 80 righe (30 per Milano/Roma, 20 per Torino)

# --[configurazioni base]--
tipi_bici = ["classica", "elettrica"]
anni = [2020, 2021, 2022, 2023, 2024]
bici_data = []

# distribuzioni bici realistiche rispetto a df_corse
distribuzione_bici = {
    "Milano":   30,
    "Roma":     30,
    "Torino":   20}

# contatori separati per città
contatori_citta = {
    "Milano":   1,
    "Roma":     1,
    "Torino":   1}

# --[generazione dati]--
for citta, quantita in distribuzione_bici.items():
    sigla = {
        "Milano":   "MI",
        "Roma":     "RM",
        "Torino":   "TO"
        }[citta]
    for _ in range(quantita):
        numero_bici = contatori_citta[citta]
        contatori_citta[citta] += 1

        # distribuzione classiche più numerose delle elettriche
        tipo = random.choices(
            population = tipi_bici,
            weights = [0.65, 0.35])[0]
        
        anno = random.choice(anni)

        # costi realistici
        if tipo == "classica":
            # bici classiche: circa 250€ - 500€ 
            costo = round(np.random.uniform(low = 250, high = 500), 2)
        else:
            # bici elettriche: circa 1200€ - 2800€
            costo = round(np.random.uniform(low = 1200, high = 2800), 2)

        bici_data.append(
            (f"{sigla}-{numero_bici:03d}",
            tipo,
            citta,
            anno,
            costo))

# --[creazione DataFrame]--
df_bici = pd.DataFrame(bici_data, columns = [
    "id_bici",
    "tipo",
    "citta",
    "anno",
    "costo"])


# [ 3 ] df_utenti: 25 righe

# --[configurazioni base]--
nomi = ["Luca", "Marco", "Giulia", "Anna", "Francesca",
        "Davide", "Alessandro", "Sara", "Matteo", "Chiara",
        "Stefano", "Elena", "Simone", "Martina", "Paolo",
        "Federica", "Andrea", "Valentina", "Riccardo", "Laura",
        "Giorgio", "Beatrice", "Fabio", "Marta", "Daniele",
        "Irene", "Emanuele", "Camilla", "Filippo", "Silvia"]
cognomi = ["Rossi", "Bianchi", "Romano", "Ricci", "Marino",
        "Greco", "Bruno", "Gallo", "Conti", "De Luca",
        "Mancini", "Costa", "Giordano", "Rizzo", "Lombardi",
        "Moretti", "Barbieri", "Fontana", "Santoro", "Mariani",
        "Caruso", "Ferrara", "Leone", "Serra", "Villa",
        "Ferri", "Longo", "Martinelli", "Testa", "Sala"]
citta_config = {
    "Milano":   {"sigla":       "MI",
                 "n_utenti":    25},
    "Roma":     {"sigla":       "RM",
                 "n_utenti":    15},
    "Torino":   {"sigla":       "TO",
                 "n_utenti":    10}}
tipi_abbonamento = [
    "Basic",
    "Premium",
    "Student"]

# distribuzione realistica
weights_abbonamenti = [0.45, 0.25, 0.30]

# periodo iscrizioni
date_iscrizione = pd.date_range(
    start = "2026-04-01",
    end =   "2026-05-15",
    freq =  "D")

utenti_data = []

# --[generazione utenti]--
for citta, config in citta_config.items():
    sigla = config["sigla"]
    
    for i in range(1, config["n_utenti"] + 1):
        nome_completo = (
            f"{random.choice(nomi)} "
            f"{random.choice(cognomi)}")
        
        tipo_abbonamento = random.choices(
            tipi_abbonamento,
            weights = weights_abbonamenti)[0]

        data_iscrizione = random.choice(date_iscrizione).strftime("%Y-%m-%d")
        
        utenti_data.append(
            (f"U-{sigla}-{i:02d}",
            nome_completo,
            citta,
            tipo_abbonamento,
            data_iscrizione))

# --[creazione DataFrame]--
df_utenti = pd.DataFrame(utenti_data, columns = [
    "id_utente",
    "nome",
    "citta",
    "tipo_abbonamento",
    "data_iscrizione"])

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