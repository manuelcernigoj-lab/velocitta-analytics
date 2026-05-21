"""
Task 5 — Analisi Numerica con NumPy
 
Contenuto:
    5.1 — Generazione dati       : durate, km, velocita
    5.2 — Slicing e selezione    : fancy indexing, maschere booleane
    5.3 — Statistiche            : percentili, normalizzazione, correlazione Pearson
    5.4 — Serie temporale        : media mobile, picco max/min, riepilogo tabellare
"""

import numpy as np

# --[generazione dati]--
np.random.seed(42)
# ↘ seed fisso → risultati riproducibili ad ogni esecuzione

# durate: 500 interi da distribuzione normale (media = 28, std = 12), minimo 1
durate = np.random.normal(loc = 28,     # media
                          scale = 12,   # std
                          size = 500    # quantità
                          ).astype(int) # trasforma in interi
durate = np.clip(durate, 
                 1,         # clip: porta a 1 tutti i valori < 1
                 None)      # None = nessun limite superiore
 
# km: proporzionali alle durate con fattore casuale uniforme tra 0.15 e 0.25
km = durate * np.random.uniform(low = 0.15,     # minimo
                                high = 0.25,    # massimo
                                size = 500)     # quantità (= a durate)
km = np.round(km, 2)    # arrotondamento
 
# velocita: km/h → converte durate da minuti a ore prima di dividere
velocita = km / (durate / 60)
velocita = np.round(velocita, 2)

# --[prints]--
data = [("durate", durate), ("km", km), ("velocita", velocita)]
# ↘ lista di tuple nome, arr per print sequenziali nel ciclo for

print(f"[ 5.1 ] — Generazione dati")
for nome, arr in data:
    print(f"\n  ───[ {nome} ]───")
    print(f"  shape : {arr.shape}")
    print(f"  dtype : {arr.dtype}")
    print(f"  min   : {arr.min():.2f}")
    print(f"  max   : {arr.max():.2f}")
    print(f"  media : {arr.mean():.2f}")
    print(f"  std   : {arr.std():.2f}")

# --[slicing e selezione]--
print(f"\n[ 5.2 ] — Slicing e selezione")

# --[prime e ultime 10 corse] --
prime_10  = durate[:10]
ultime_10 = durate[-10:]
 
print(f"\n• Prime 10 durate  : {prime_10}")
print(f"• Ultime 10 durate : {ultime_10}")
 
# --[fancy indexing: selezione per lista di indici arbitrari]--
indici = [0, 42, 99, 150, 200, 350, 499]
selezione = durate[indici]
 
print(f"\n• Fancy indexing — indici {indici}:")
print(f"  durate : {selezione}")
 
# --[maschera booleana: corse con durata > 45 min (lunghe)]--
maschera_lunghe = durate > 45
corse_lunghe    = durate[maschera_lunghe]
km_lunghe       = km[maschera_lunghe]       # stessa maschera applicata a km
 
print(f"\n• Corse con durata > 45 min:")
print(f"  numero corse  : {maschera_lunghe.sum()}")     # True conta come 1
print(f"  distanza media: {km_lunghe.mean():.2f} km")
 
# --[indice corsa con velocità massima e minima]--
idx_max = np.argmax(velocita)
idx_min = np.argmin(velocita)
# ↘ argmax/argmin per ottenere l'indice invece che il valore
 
print(f"\n• Velocità massima: {velocita[idx_max]:.2f} km/h → corsa indice {idx_max}")
print(f"• Velocità minima : {velocita[idx_min]:.2f} km/h → corsa indice {idx_min}")

# --[statistiche e normalizzazione]--
print(f"\n[ 5.3 ] — Statistiche e normalizzazione")

# --[percentili]--
p25, p50, p75, p90 = np.percentile(durate, [25, 50, 75, 90])
 
print(f"\n• Percentili durate:")
print(f"  25°  : {p25:.1f} min")
print(f"  50°  : {p50:.1f} min")
print(f"  75°  : {p75:.1f} min")
print(f"  90°  : {p90:.1f} min")
 
# --[normalizzazione min-max]--
durate_norm = (durate - durate.min()) / (durate.max() - durate.min())
# ↘ scala tutti i valori nell'intervallo [0, 1]
 
# verifica che i valori siano effettivamente in [0, 1]
print(f"\n• Normalizzazione min-max durate:")
print(f"  min normalizzato : {durate_norm.min():.2f}  (atteso: 0.0)")
print(f"  max normalizzato : {durate_norm.max():.2f}  (atteso: 1.0)")
print(f"  media normalizzata: {durate_norm.mean():.2f}")
 
# --[correlazione di Pearson tra durate e km (solo NumPy)]--
matrice_corr = np.corrcoef(durate, km)
# ↘ np.corrcoef restituisce una matrice 2×2:
#   [[corr(durate,durate), corr(durate,km)],
#    [corr(km,durate),     corr(km,km)   ]]

pearson_r    = matrice_corr[0, 1]
# ↘ il valore di correlazione durate-km è l'elemento [0, 1]
 
print(f"\n• Correlazione di Pearson durate-km: {pearson_r:.2f}")

# --[serie temporale simulata]--
print(f"\n[ 5.4 ] — Serie temporale simulata")

# --[generazione: corse giornaliere per 30 giorni]--
corse_giornaliere = np.random.randint(low = 80, high = 200, size = 30)
 
# --[media mobile a 7 giorni]--
gg = 7
media_mobile_allineata = np.full(30, np.nan)   # array di 30 NaN

for i in range(gg - 1, 30):     # parte dal giorno 6
    media_mobile_allineata[i] = np.mean(corse_giornaliere[i - gg + 1 : i + 1])
    # ↘ slice [i-6 : i+1] → finestra di 7 giorni che termina al giorno i
 
# --[picco massimo e minimo]--
giorno_max = np.argmax(corse_giornaliere) + 1
giorno_min = np.argmin(corse_giornaliere) + 1
 
print(f"\n• Picco massimo: giorno {giorno_max} — {corse_giornaliere[giorno_max-1]} corse")
print(f"• Picco minimo : giorno {giorno_min} — {corse_giornaliere[giorno_min-1]} corse")
 
# --[riepilogo tabellare]--
print(f"\n{'Giorno':>7} {'Corse':>7} {'Media 7gg':>10}")
print("-" * 27)
for i in range(30):
    mm = media_mobile_allineata[i]
    mm_str = f"{mm:>10.1f}"
    print(f"{i+1:>7} {corse_giornaliere[i]:>7} {mm_str}")