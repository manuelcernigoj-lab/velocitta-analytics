# VeloCittà Analytics

<p align="center">
  <img src="assets/velocitta_banner.png" alt="VeloCittà Banner" width="750"/>
</p>

**Autore:** Manuel Cernigoj

---

## Descrizione

VeloCittà Analytics è un progetto di analisi dati end-to-end simulato per una startup italiana di bike sharing attiva a Milano, Roma e Torino. Il sistema copre l'intero pipeline analitico: modellazione OOP del dominio (flotta biciclette, utenti, corse), analisi numerica con NumPy, pulizia e aggregazione dati con Pandas, query SQL sul database operativo e visualizzazione dei risultati. L'obiettivo è fornire insight sul comportamento degli utenti, sull'utilizzo della flotta e sui ricavi stimati per città, simulando il lavoro di un analista junior in contesto reale.

---

## Struttura del progetto

```
velocitta-analytics/
├── 01_python_scripts/
│   ├── task1_utils.py
│   ├── task2_models.py
│   ├── task5_numpy.py
│   ├── task6_pandas.py
│   ├── task7_viz.py
├── 02_sql_files/
│   ├── create_tables.sql
│   ├── insert_values.sql
│   ├── task4_sql.sql
├── assets/
│   └── velocitta_banner.png
├── output/
│   ├── 01_serie_temporale.png
│   ├── 01b_corse_per_giorno.png
│   ├── 02_distribuzione_durate.png
│   ├── 03_fasce_orarie.png
│   ├── 04_scatter_durata_velocita.png
│   ├── 05_dashboard.png
│   └── 06_corse_per_giorno.png
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Installazione

```bash
pip install -r requirements.txt
```

---

## Esecuzione

Gli script vanno eseguiti nell'ordine indicato — ogni modulo dipende dal precedente.

```bash
# 1. funzioni di utilità (nessuna dipendenza esterna)
python task1_utils.py

# 2. modelli OOP — Bicicletta e FlottaBici + ereditarietà, incapsulamento, polimorfismo
python task2_models.py

# 3. query SQL — eseguire con sqlite3 o MySQL Workbench
sqlite3 velocita.db < task4_sql.sql

# 4. analisi numerica con NumPy
python task5_numpy.py

# 5. pulizia e analisi con Pandas
python task6_pandas.py

# 6. visualizzazione — genera i grafici in output/
python task7_viz.py
```

---

## Grafici generati

| # | File | Contenuto |
|---|------|-----------|
| 1 | `01_serie_temporale.png` | Corse giornaliere per città — 15 giorni |
| 1b | `01b_corse_per_giorno.png` | Corse aggregate per giorno della settimana |
| 2 | `02_distribuzione_durate.png` | Distribuzione durate corse con KDE per città |
| 3 | `03_fasce_orarie.png` | Corse per fascia oraria e tipo bicicletta |
| 4 | `04_scatter_durata_velocita.png` | Scatter durata vs velocità con linea di tendenza |
| 5 | `05_dashboard.png` | Dashboard riepilogativa 2×2 |

---

## Considerazioni

Il task più impegnativo è stato la gestione della pipeline OOP: definire correttamente i confini tra classe base e sottoclassi, e decidere dove collocare la logica di validazione (nella classe base vs nelle sottoclassi), ha richiesto diversi cicli di revisione. Il pattern `cerca_per_id` come metodo fondante di `FlottaBici` — su cui poggiano `aggiungi`, `rimuovi` e le statistiche — si è rivelato la scelta architetturale più utile per mantenere il codice coerente.

Sul fronte Pandas, il metodo `groupby + transform` per la sostituzione dei NaN con la mediana per città è stato il passaggio più interessante: a differenza di un semplice `fillna(mediana_globale)`, rispetta la distribuzione locale di ogni città, producendo imputazioni più realistiche.

Un'osservazione sui dati: la correlazione di Pearson tra durata e km (~0.97) è attesa per costruzione, ma in dati reali sarebbe significativamente più bassa — fattori come traffico, tipo di percorso e stile di guida introdurrebbero varianza che il dataset simulato non cattura. Una direzione di miglioramento sarebbe arricchire il dataset con variabili contestuali (meteo, ora del giorno, tipo di stazione) per rendere le analisi più realistiche e i modelli predittivi più robusti.

---

## Requirements

```
numpy~=2.0
pandas~=2.2
matplotlib~=3.8
seaborn~=0.13
```