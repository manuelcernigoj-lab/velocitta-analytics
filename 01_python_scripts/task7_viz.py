"""
Task 7 — Visualizzazione

Contenuto:
    Grafico 1 — Serie temporale corse per città         → output/01_serie_temporale.png
    Grafico 2 — Distribuzione durate per città          → output/02_distribuzione_durate.png
    Grafico 3 — Corse per fascia oraria e tipo bici     → output/03_fasce_orarie.png
    Grafico 4 — Scatter durata vs velocità              → output/04_scatter_durata_velocita.png
    Grafico 5 — Dashboard riepilogativa (2×2)           → output/05_dashboard.png

Palette VeloCittà:
    Milano  #3DBFB8  teal
    Roma    #F5C842  giallo
    Torino  #5B8DB8  blu
    neutri  teal / blu / verde scuro (#2E8B57)
    trend   #F5C842  giallo (contrasto su scatter)
"""

import os
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
import pandas as pd
import numpy as np

# importa df_corse, df_bici, df_utenti già puliti da task6
from task6_pandas import df_corse, df_bici, df_utenti, df_merged

# --[cartella output]--
os.makedirs("output", exist_ok = True)

# --[palette]--
COLORI_CITTA = {
    "Milano": "#3DBFB8",
    "Roma":   "#F5C842",
    "Torino": "#5B8DB8",
}
COLORI_NEUTRI = ["#3DBFB8", "#5B8DB8", "#2E8B57"]
COLORE_TREND  =  "#F5C842"

# --[stile globale]--
# rcParams globali: font size e peso titoli uniformi su tutti i grafici
sns.set_style("white")              # sfondo bianco, niente griglie
plt.rcParams.update({
    "figure.figsize":       (10, 6),
    "font.size":            11,
    "axes.titlesize":       13,
    "axes.titleweight":     "bold",
    "axes.labelweight":     "bold",
    "axes.spines.top":      False,
    "axes.spines.right":    False})



# [ GRAFICO 1 ] — serie temporale corse per città
# ↘ domanda di business: come si distribuisce nel tempo l'utilizzo del servizio
#   nelle tre città? Si notano picchi o stagionalità settimanali?

# --[aggregazione corse per data e città]--
serie = (
    df_corse
    .groupby(["data_corsa", "citta"])["id_corsa"]
    .count()
    .reset_index()
    .rename(columns={"id_corsa": "n_corse"}))
serie["giorno"] = serie["data_corsa"].dt.day

# --[creazione figura]--
fig, ax = plt.subplots()

# --[creazione serie temporali sovrapposte]--
for citta, colore in COLORI_CITTA.items():
    dati = serie[serie["citta"] == citta].sort_values("data_corsa")
    ax.plot(dati["giorno"],
            dati["n_corse"],
            label = citta,
            color = colore, 
            linewidth = 2,
            marker = "o",
            markersize = 4)

# --[intestazioni/formattazioni]--
ax.set_title("Corse giornaliere per città")
ax.set_xticks(range(1, 16))     # tick per ogni giorno da 1 a 15
ax.set_xlabel("Giorno (aprile 2026)")
ax.set_ylabel("Numero corse")
ax.legend(title = "Città", frameon = False)
ax.yaxis.set_major_locator(mticker.MaxNLocator(integer = True))

# ↘ forza l'asse Y a mostrare solo numeri interi come tick
fig.tight_layout()

# --[export]--
fig.savefig("output/01_serie_temporale.png", dpi = 150)
plt.close(fig)
# ↘ chiude la figura e libera la memoria
print("✓ Grafico 1 salvato")

# [ GRAFICO 1b ] — corse aggregate per giorno della settimana
# ↘ Domanda di business: quali giorni della settimana hanno più utilizzo per città?

# --[aggregazione corse per giorno_settimana e città]--
ordine_giorni = ["Lunedì", "Martedì", "Mercoledì", "Giovedì", "Venerdì", "Sabato", "Domenica"]
agg_giorno = (
    df_corse
    .groupby(["giorno_settimana", "citta"])["id_corsa"]
    .count()
    .reset_index()
    .rename(columns = {"id_corsa": "n_corse"}))

agg_giorno["giorno_settimana"] = pd.Categorical(
    agg_giorno["giorno_settimana"],
    categories = ordine_giorni,
    ordered = True)
    # ↘ converte giorno_settimana in Categorical con ordine fisso
    #   senza questo, seaborn ordina alfabeticamente
agg_giorno = agg_giorno.sort_values("giorno_settimana")

# --[creazione figura]--
fig, ax = plt.subplots()

# --[creazione barplots raggruppati per giorno della settimana]--
sns.barplot(
    data    = agg_giorno,
    x       = "giorno_settimana",
    y       = "n_corse",
    hue     = "citta",
    palette = COLORI_CITTA,
    ax      = ax)

# --[intestazioni/formattazioni]--
ax.set_title("Corse per giorno della settimana e città")
ax.set_xlabel("Giorno")
ax.set_ylabel("Numero corse")
ax.legend(title = "Città", frameon = False)
fig.tight_layout()

# --[export]--
fig.savefig("output/01b_corse_per_giorno.png", dpi = 150)
plt.close(fig)
print("✓ Grafico 1b salvato")

# [ GRAFICO 2 ] — distribuzione durate per città
# ↘ Domanda di business: la durata media di una corsa varia tra città?

# --[creazione figura]--
fig, ax = plt.subplots()

# --[creazione histplot raggruppati per giorno della settimana]--
sns.histplot(
    data    = df_corse,
    x       = "durata_minuti",
    hue     = "citta",
    kde     = True,                         # aggiunge curva di densità
    palette = COLORI_CITTA,
    alpha   = 0.45,                         # trasparenza per leggere sovrapposizioni
    bins    = 30,
    ax      = ax)

# --[intestazioni/formattazioni]--
ax.set_title("Distribuzione durate per città")
ax.set_xlabel("Durata (minuti)")
ax.set_xticks(range(5, 65, 5))     # tick da 5 a 60 inclusi ogni 5 minuti
ax.set_ylabel("Numero corse")
legend = ax.legend_
legend.set_title("Città")
legend.set_frame_on(False)
fig.tight_layout()

# --[export]--
fig.savefig("output/02_distribuzione_durate.png", dpi = 150)
plt.close(fig)
print("✓ Grafico 2 salvato")

# [ GRAFICO 3 ] — corse per fascia oraria e tipo bicicletta
# ↘ Domanda di business: in quale fascia oraria si concentra l'utilizzo?
#   Il tipo di bici influenza la fascia preferita?

# --[merge con df_bici per avere il tipo bici nelle corse]--
df_corse_tipo = df_corse.merge(df_bici[["id_bici", "tipo"]], on = "id_bici", how = "left")
ordine_fasce = ["mattina", "pomeriggio", "sera"]

# --[aggregazione corse per fascia oraria e tipo bici]--
bar = (
    df_corse_tipo
    .groupby(["fascia_oraria", "tipo"])["id_corsa"]
    .count()
    .reset_index()
    .rename(columns = {"id_corsa": "n_corse"}))

# --[creazione figura]--
fig, ax = plt.subplots()

# --[creazione histplot raggruppati per giorno della settimana]--
sns.barplot(
    data    = bar,
    x       = "fascia_oraria",
    y       = "n_corse",
    hue     = "tipo",
    order   = ordine_fasce,
    palette = {"classica": "#3DBFB8", "elettrica": "#5B8DB8"},  # teal vs blu — ben separati
    ax      = ax)

# --[intestazioni/formattazioni]--
ax.set_title("Corse per fascia oraria e tipo bicicletta")
ax.set_xlabel("Fascia oraria")
ax.set_ylabel("Numero corse")
ax.legend(title = "Tipo bici", frameon = False)
fig.tight_layout()

# --[export]--
fig.savefig("output/03_fasce_orarie.png", dpi = 150)
plt.close(fig)
print("✓ Grafico 3 salvato")

# [ GRAFICO 4 ] — scatter durata vs velocità con linea di tendenza
# ↘ Domanda di business: è vero che la durata della corsa è inversamente 
#   proporzionale alla velocità?

# --[creazione figura]--
fig, ax = plt.subplots()

# --[creazione histplot raggruppati per giorno della settimana]--
ax.scatter(df_corse["durata_minuti"], df_corse["velocita_media"],
           color = "#3DBFB8", alpha = 0.7, s = 50, edgecolors="none")

# --[trendline]--
x = df_corse["durata_minuti"].values
y = df_corse["velocita_media"].values
coefficienti = np.polyfit(x, y, deg = 1)           # restituisce [m, q] della retta y=mx+q
retta        = np.poly1d(coefficienti)             # creazione della funzione retta(x) → y
x_range      = np.linspace(x.min(), x.max(), 100)  # creazione dei punti x della retta
 
ax.plot(x_range,
        retta(x_range),         # utilizzo della funzione per ricavare y
        color = COLORE_TREND,
        linewidth = 2,
        linestyle = "--",
        label = "Trend")

# --[intestazioni/formattazioni]--
ax.set_title("Durata vs velocità media per città")
ax.set_xlabel("Durata (minuti)")
ax.set_ylabel("Velocità media (km/h)")
ax.legend(frameon = False)
fig.tight_layout()

# --[export]--
fig.savefig("output/04_scatter_durata_velocita.png", dpi = 150)
plt.close(fig)
print("✓ Grafico 4 salvato")

# [ GRAFICO 5 ] — dashboard riepilogativa (2x2)

# --[creazione figura che conterrà tutti i plots]--
fig, axes = plt.subplots(2, 2, figsize = (10, 8))
fig.suptitle("Dashboard VeloCittà - Riepilogo", fontsize = 15, fontweight = "bold", y = 1.01)

# --[in alto sx (↖): bar chart corse per città]--
ax = axes[0, 0]
corse_citta = df_corse.groupby("citta")["id_corsa"].count()
 
ax.bar(corse_citta.index, corse_citta.values,
       color = [COLORI_CITTA[c] for c in corse_citta.index])

# --[intestazioni/formattazioni]--
ax.set_title("Corse per città")
ax.set_xlabel("Città")
ax.set_ylabel("Numero corse")
ax.yaxis.set_major_locator(mticker.MaxNLocator(integer=True))

# --[in alto dx (↗): pie chart abbonamenti utenti]--
ax = axes[0, 1]
abbonamenti = df_utenti["tipo_abbonamento"].value_counts()
ax.pie(
    abbonamenti.values,
    labels      = abbonamenti.index,
    colors      = COLORI_NEUTRI,
    autopct     = "%1.0f%%",
    startangle  = 90,
    wedgeprops  = {"linewidth": 1, "edgecolor": "white"})

# --[intestazioni/formattazioni]--
ax.set_title("Distribuzione abbonamenti")

# --[in basso sx (↙): bar chart costo totale per città]--
ax = axes[1, 0]
costo_citta = (
    df_corse
    .groupby("citta")["costo_stimato"]
    .sum()
    .round(2))
 
ax.bar(costo_citta.index, costo_citta.values,
       color = [COLORI_CITTA[c] for c in costo_citta.index])

# --[intestazioni/formattazioni]--
ax.set_title("Ricavo stimato per città (€)")
ax.set_xlabel("Città")
ax.set_ylabel("Costo totale (€)")

# --[in basso dx (↘): boxplot durate per tipo corsa]--
ax = axes[1, 1]

ordine_tipo  = ["breve", "media", "lunga"]
sns.boxplot(
    data      = df_corse,
    x         = "tipo_corsa",
    y         = "durata_minuti",
    order     = ordine_tipo,
    hue       = "tipo_corsa",
    palette   = COLORI_NEUTRI,
    width     = 0.5,
    linewidth = 0.8,
    ax        = ax)

# --[intestazioni/formattazioni]--
ax.set_title("Durate per tipo corsa")
ax.set_xlabel("Tipo corsa")
ax.set_ylabel("Durata (minuti)")

fig.tight_layout()

# --[export]--
fig.savefig("output/05_dashboard.png", dpi=150, bbox_inches="tight")
plt.close(fig)
print("✓ Grafico 5 salvato")
 
print("\n✓ Tutti i grafici salvati in output/")