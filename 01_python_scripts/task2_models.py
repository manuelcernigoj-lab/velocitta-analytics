"""
Parte 1: Record e Dataset
Creazione:
    - Classe Bicicletta — pattern Record
    - Classe FlottaBici — pattern Dataset
"""
"""
Parte 2: Ereditarietà, Incapsulamento, Polimorfismo
Creazione sottoclassi:
    - BiciclettaClassica(Bicicletta)
    - BiciclettaElettrica(Bicicletta)
"""

# import del modulo per validare il formato id_bici
from task1_utils import valida_id_bici

# --[creazione classe Record 'Bicicletta']--
class Bicicletta:

    # --[costruttore]--
    def __init__(self,
                 id_bici:           str,        # formato: "AA-000"
                 tipo:              str,        # formato: "classica"/"elettrica"
                 stazione_corrente: str,        # formato: "Cadorna"/"Loreto"/...
                 km_percorsi:       float,      # formato: 0.0 (km)
                 disponibile:       bool,):     # formato: True/False
        
        # --[validazione id_bici, prima dell'assegnazione]--
        valida_id_bici(id_bici)

        # --[verifica che il 'tipo' sia corretto]--
        if tipo not in ("classica", "elettrica", "cargo"):
            raise ValueError(f"Tipo non valido '{tipo}': atteso 'classica', 'elettrica' o 'cargo'")

        self.id_bici =              id_bici
        self.tipo =                 tipo
        self.stazione_corrente =    stazione_corrente
        self._km_percorsi =         km_percorsi
        # ↘ edit: km_percorsi → _km_percorsi 
        #         (attributo protetto richiesto al punto 3.2)
        self.disponibile =          disponibile
        self.utente_corrente =      None        # popolato da noleggia(), svuotato da restituisci()
    
    # --[getter: @property espone _km_percorsi in sola lettura]--
    @property
    def km_percorsi(self) -> float:
        return self._km_percorsi
    
    # --[aggiungi_km: unico modo per modificare _km_percorsi dall'esterno]--
    def aggiungi_km(self, km: float) -> None:
        # valida che km > 0 prima di aggiornare, impedendo valori negativi o zero
        if km <= 0:
            raise ValueError(f"km deve essere > 0, ricevuto {km}")
        self._km_percorsi += km
    
    # --[blocca la bici per l'utente]--
    def noleggia(self,
                 utente:    str     # formato "Mario Rossi"
                 ) -> str:
        
        # --[verifica se disponibile, altrimenti solleva 'ValueError']--
        if not self.disponibile:
            raise ValueError(f"Bici {self.id_bici} già in uso")

        # --[imposta disponibile = False e utente_corrente = utente]--
        self.disponibile = False
        self.utente_corrente = utente       # tracciamento di chi l'ha presa
    
        return f"Bici {self.id_bici} noleggiata da {utente}"

    # --[rende la bici nuovamente disponibile]
    def restituisci(self,
                    stazione:       str,    # formato: "Cadorna"/"Loreto"/...
                    km_aggiunta:    float   # formato: 0.0 (km)
                    ) -> None:
        
        # --[verifica se stazione esiste, altrimenti solleva 'ValueError']--
        if not stazione or not stazione.strip():
            raise ValueError(f"Stazione {stazione} non presente")
        
        # --[verifica se km_aggiunta è positivo, altrimenti solleva 'ValueError']--
        if km_aggiunta < 0:
            raise ValueError(f"Km inseriti '{km_aggiunta}' non validi, inserire un numero positivo")
        
        # --[aggiorna posizione | somma km_aggiunta | imposta disponibile = True | reset di utente_corrente]--
        self.stazione_corrente =    stazione
        self.aggiungi_km(km_aggiunta)
        # ↘ update: ora usa 'aggiungi_km()' per accedere a '_km_percorsi'
        self.disponibile =          True
        self.utente_corrente =      None
    
    # --[usato da print(), mostra solo le info utili all'utente]--
    def __str__(self) -> str:
        stato = "✓ disponibile" if self.disponibile else f"✗ in uso da {self.utente_corrente}"
        return f"[{self.id_bici}] {self.tipo} | {self.stazione_corrente} | {self.km_percorsi:.1f} km | {stato}"

    # --[usato per debugging dallo sviluppatore]--
    def __repr__(self) -> str:
        return (f"Bicicletta(id_bici = '{self.id_bici}', tipo = '{self.tipo}', "
                f"stazione_corrente = '{self.stazione_corrente}', "
                f"km_percorsi = {self.km_percorsi}, disponibile = {self.disponibile})")

# --[creazione sottoclasse_1 'BiciclettaClassica']--
class BiciclettaClassica(Bicicletta):
    """
    Sottoclasse di Bicicletta per bici classiche (non elettriche).
    Aggiunge l'attributo taglia ('S', 'M', 'L').
    """
 
    TAGLIE_VALIDE = ("S", "M", "L")
    # ↘ costante di classe: valori ammessi per taglia
 
    def __init__(self,
                 id_bici:           str,
                 stazione_corrente: str,
                 km_percorsi:       float,
                 disponibile:       bool,
                 taglia:            str):
                 # ↘ attributo aggiuntivo rispetto alla classe base

        # richiama __init__ della classe base passando tipo = "classica"
        super().__init__(id_bici, 
                        "classica",
                        stazione_corrente,
                        km_percorsi,
                        disponibile)
        
        # --[verifica validità di 'taglia' prima dell'assegnazione]--
        if taglia not in self.TAGLIE_VALIDE:
            raise ValueError(f"Taglia non valida '{taglia}': atteso {self.TAGLIE_VALIDE}")
        self.taglia = taglia
    
    # --[override di __str__ e __repr__: aggiunge taglia all'output]--
    def __str__(self) -> str:
        stato = "✓ disponibile" if self.disponibile else f"✗ in uso da {self.utente_corrente}"
        return (f"[{self.id_bici}] classica | taglia {self.taglia} | "
                f"{self.stazione_corrente} | {self._km_percorsi:.1f} km | {stato}")
 
    def __repr__(self) -> str:
        return (f"BiciclettaClassica(id_bici = '{self.id_bici}', "
                f"stazione_corrente = '{self.stazione_corrente}', "
                f"km_percorsi = {self._km_percorsi}, disponibile = {self.disponibile}, "
                f"taglia = '{self.taglia}')")

# --[creazione sottoclasse_2 'BiciclettaElettrica']--
class BiciclettaElettrica(Bicicletta):   
    """
    Sottoclasse di Bicicletta per bici elettriche.
    Aggiunge batteria_percentuale (0-100) e metodo ricarica().
    Override di noleggia() per bloccare il noleggio sotto il 20% di batteria.
    """

    BATTERIA_MIN_NOLEGGIO = 20
    # ↘ costante di classe: soglia minima per il noleggio

    def __init__(self,
                 id_bici:               str,
                 stazione_corrente:     str,
                 km_percorsi:           float,
                 disponibile:           bool,
                 batteria_percentuale:  int):
                 # ↘ attributo aggiuntivo rispetto alla classe base
 
        # richiama __init__ della classe base passando tipo = "elettrica"
        super().__init__(id_bici,
                         "elettrica",
                         stazione_corrente,
                         km_percorsi,
                         disponibile)

        # --[verifica validità di 'batteria_percentuale' prima dell'assegnazione]--
        if not (0 <= batteria_percentuale <= 100):
            raise ValueError(f"Batteria non valida ({batteria_percentuale}): atteso 0-100")
        self.batteria_percentuale = batteria_percentuale

    # --[override di noleggia: aggiunge controllo batteria minima]--
    def noleggia(self, utente: str) -> str:
        if self.batteria_percentuale < self.BATTERIA_MIN_NOLEGGIO:
            raise ValueError(
                f"Batteria insufficiente ({self.batteria_percentuale}%): "
                f"minimo {self.BATTERIA_MIN_NOLEGGIO}% per il noleggio"
            )
        return super().noleggia(utente)
               # ↘ richiama il metodo della classe base per non riscrivere
               #   la logica di disponibilità già implementata
    
    # --[metodo aggiuntivo: ricarica la batteria fino a un massimo di 100%]--
    def ricarica(self, percentuale: int) -> None:
        
        # --[verifica validità di 'percentuale' prima di procedere]--
        if not (0 <= percentuale <= 100):
            raise ValueError(f"Percentuale non valida ({percentuale}): atteso 0-100")
        
        # --[seconda verifica 'percentuale' deve essere maggiore del valore attuale]--
        if percentuale <= self.batteria_percentuale:
            raise ValueError(
                f"Percentuale impostata ({percentuale}%) deve essere maggiore "
                f"della carica attuale ({self.batteria_percentuale}%)"
                )
        self.batteria_percentuale = percentuale     # aggiorna batteria_percentuale
 
    # --[override di __str__ e __repr__: aggiunge livello batteria all'output]--
    def __str__(self) -> str:
        stato = "✓ disponibile" if self.disponibile else f"✗ in uso da {self.utente_corrente}"
        return (f"[{self.id_bici}] elettrica | 🔋 {self.batteria_percentuale}% | "
                f"{self.stazione_corrente} | {self._km_percorsi:.1f} km | {stato}")
 
    def __repr__(self) -> str:
        return (f"BiciclettaElettrica(id_bici = '{self.id_bici}', "
                f"stazione_corrente = '{self.stazione_corrente}', "
                f"km_percorsi = {self._km_percorsi}, disponibile = {self.disponibile}, "
                f"batteria_percentuale = {self.batteria_percentuale})")

# --[creazione sottoclasse_3 (extra) 'BiciclettaCargo']--
class BiciclettaCargo(Bicicletta):   
    """
    Sottoclasse aggiuntiva per bici cargo (trasporto merci).
    Aggiunge portata_max_kg e override di noleggia() con controllo peso carico.
    """

    PORTATE = {
        "leggera": 50.0,
        "pesante": 100.0
        }
    # ↘ costanti di classe — portate predefinite per categoria

    def __init__(self,
                 id_bici:           str,
                 stazione_corrente: str,
                 km_percorsi:       float,
                 disponibile:       bool,
                 categoria:         str):
                 # ↘ attributo aggiuntivo "leggera"/"pesante"

        super().__init__(id_bici,
                         "cargo",
                         stazione_corrente,
                         km_percorsi,
                         disponibile)

        # --[verifica validità di 'categoria' prima dell'assegnazione]--
        if categoria not in self.PORTATE:
            raise ValueError(f"Categoria non valida '{categoria}': atteso {list(self.PORTATE.keys())}")
        
        self.categoria = categoria
        self.portata_max_kg = self.PORTATE[categoria]   # assegnato automaticamente dalla categoria

    # --[override di noleggia: aggiunge parametro peso_carico]--
    def noleggia(self,
                 utente: str,
                 peso_carico: float = 0.0   # formato: 0.0 kg
                 ) -> str:
        
        # --[verifica su 'peso_carico' prima di procedere]--
        if peso_carico > self.portata_max_kg:
            raise ValueError(
                f"Carico ({peso_carico} kg) supera la portata massima "
                f"per categoria '{self.categoria}' ({self.portata_max_kg} kg)"
            )
        return super().noleggia(utente)
               # ↘ richiama il metodo della classe base

    # --[override di __str__ e __repr__: aggiunge portata all'output]--
    def __str__(self) -> str:
        stato = "✓ disponibile" if self.disponibile else f"✗ in uso da {self.utente_corrente}"
        return (f"[{self.id_bici}] cargo {self.categoria} | "
                f"portata {self.portata_max_kg} kg | "
                f"{self.stazione_corrente} | {self._km_percorsi:.1f} km | {stato}")
    
    def __repr__(self) -> str:
        return (f"BiciclettaCargo(id_bici = '{self.id_bici}', "
                f"stazione_corrente = '{self.stazione_corrente}', "
                f"km_percorsi = {self._km_percorsi}, disponibile = {self.disponibile}, "
                f"portata_max_kg = {self.portata_max_kg})")

# --[creazione classe Dataset 'FlottaBici']--
class FlottaBici:

    # --[costruttore]--
    def __init__(self, 
                 citta: str         # formato: "Milano"/"Roma"/"Torino"
                 ):
        self.citta =        citta
        self.biciclette =   []      # lista vuota, popolata con aggiungi()

    # --[definito all'inizio in modo che si possa riusare nei metodi successivi]--
    def cerca_per_id(self,
                     id_bici: str   # formato: "AA-000"
                     )-> Bicicletta:
        
        # --[validazione del parametro in ingresso]--
        valida_id_bici(id_bici)

        # --[match con gli elementi della lista in un ciclo for]--
        for b in self.biciclette:
            if b.id_bici == id_bici:
                return b
        raise KeyError(f"Bici {id_bici} non trovata nella flotta")
        # ↘ # se nessuna corrispondenza trovata → KeyError
        
    
    # --[aggiunge un record alla lista 'biciclette' se non presente]--
    def aggiungi(self,
                 bici: Bicicletta   # oggetto tipo 'Bicicletta'
                 ) -> None:
        
        # --[verifica se 'id_bici' esiste già, in caso solleva 'ValueError']--
        try:
            self.cerca_per_id(bici.id_bici)
            raise ValueError(f"Bici {bici.id_bici} già presente nella flotta")
            # ↘ se bici trovata → raise ValueError in quanto esiste già
        except KeyError:
            self.biciclette.append(bici)
            # ↘ se bici non trovata → intercetta KeyError ed esegue .append()

    # --[rimuove un record alla lista 'biciclette' se presente]--
    def rimuovi(self,
                id_bici: str    # formato: "AA-000"
                ) -> None:
        
        self.cerca_per_id(id_bici)
        # ↘ se bici non trovata → raise KeyError
        self.biciclette = [b for b in self.biciclette if b.id_bici != id_bici]
        # ↘ se bici trovata → ricrea la lista con list comprehension 
        #   escludendo l'id da rimuovere
    
    # --[ritorna la lista delle bici disponibili dopo confronto su 'disponibile']--
    def disponibili(self) -> list[Bicicletta]:
        return [b for b in self.biciclette if b.disponibile]
    
    # --[per usare len() direttamente sulla classe 'FlottaBici']
    def __len__(self) -> int:
        return len(self.biciclette)

    # --[calcola e ritorna delle statistiche sulla flotta di bici]
    def statistiche(self) -> dict:
        
        # --[calcolo statistiche]--
        tot =       len(self)       # usa metodo speciale __len__ direttamente su 'FlottaBici' 
        disp =      len(self.disponibili())
        uso =       tot - disp
        km_tot =    sum(b.km_percorsi for b in self.biciclette)
        km_bic =    round(km_tot / tot, 2) if tot > 0 else 0    # evita errore dividendo per zero
        
        # --[return dict]--
        return {
            "totale":               tot,
            "disponibili":          disp,
            "in_uso":               uso,
            "km_totali_flotta":     km_tot,
            "km_medi_per_bici":     km_bic
            }
        
    # --[per costruire la flotta da una lista di dizionari]--
    @classmethod
    def da_lista(cls,
                 citta: str,        # formato: "Milano"/"Roma"/"Torino" 
                 dati: list         # formato: [{"id": ..., "tipo": ..., "stazione": ..., "km": ...}]
                 ) -> "FlottaBici":
        flotta = cls(citta)         # equivale a FlottaBici(citta)
        
        # --[spacchettamento dell informazioni nella lista 'dati']--
        for d in dati:
            bici = Bicicletta(
                id_bici =            d["id"],
                tipo =               d["tipo"],
                stazione_corrente =  d["stazione"],
                km_percorsi =        d["km"],
                disponibile =        d.get("disponibile", True)
                                     # ↘ get() per impostare un valore default = True se chiave assente
                )
            
            # --[aggiunge i dati della bici corrente alla flotta]--
            flotta.aggiungi(bici)

        return flotta

# --[stampa_flotta() che sfrutta il polimorfismo]--
def stampa_flotta(biciclette: list) -> None:
    """
    Stampa le informazioni di ogni bici nella lista.
    Funziona con qualsiasi sottoclasse di Bicicletta grazie al polimorfismo:
    print() invoca __str__() della classe reale dell'oggetto.
    """
    print(f"\n{'─' * 20}[ FLOTTA — {len(biciclette)} biciclette ]{'─' * 20}")
    for b in biciclette:
        print(f"  {b}")
        # ↘ chiama b.__str__() della classe reale, non di Bicicletta
    print(f"{'─' * 65}\n")

# --[descrivi_bici() sfrutta il polimorfismo passivo tramite il 'duck typing']--
def descrivi_bici(bici) -> str:
    """
    Accetta qualsiasi oggetto che implementi id_bici, tipo e km_percorsi.
    Non importa la classe — se ha quegli attributi, funziona (duck typing).
    """
    return f"{bici.id_bici} ({bici.tipo}) — {bici.km_percorsi:.1f} km percorsi"

"""
Il polimorfismo permette di trattare oggetti di classi diverse con la stessa
interfaccia. stampa_flotta() chiama print(b) su ogni elemento, Python richiama
automaticamente il metodo __str__ corretto per ogni classe.
Questo meccanismo si chiama "dispatch dinamico": il metodo eseguito viene
scelto durante l'esecuzione del codice in base al tipo reale dell'oggetto, 
non al tipo dichiarato.
"""

# [ [esempio di chiamata] ]
if __name__ == "__main__":
 
    # istanze di classi diverse nella stessa lista
    flotta_mista = [
        BiciclettaClassica( "MI-001", "Cadorna",  120.0, True,  "M"),
        BiciclettaClassica( "MI-002", "Loreto",    85.5, True,  "S"),
        BiciclettaElettrica("MI-003", "Centrale",  340.0, True,  78),
        BiciclettaElettrica("MI-004", "Duomo",     210.0, False, 15),
        BiciclettaCargo(    "MI-005", "Garibaldi", 560.0, True,  "leggera"),
        ]
 
    # stessa funzione — output diverso per ogni tipo
    stampa_flotta(flotta_mista)
 
    # duck typing: descrivi_bici funziona su tutte le sottoclassi
    print("--- Duck typing ---")
    for b in flotta_mista:
        print(f"  {descrivi_bici(b)}")
 
    # dimostrazione ricarica BiciclettaElettrica
    print("\n--- Ricarica elettrica ---")
    ebike = BiciclettaElettrica("RM-010", "Termini", 200.0, True, 10)
    print(f"  batteria iniziale: {ebike.batteria_percentuale}%")
    try:
        ebike.noleggia("Luigi Bianchi")
        # ↘ ValueError: batteria < 20%
    except ValueError as e:
        print(f"  noleggio bloccato: {e}")
    ebike.ricarica(50)
    print(f"  dopo ricarica: {ebike.batteria_percentuale}%")
    print(f"  {ebike.noleggia('Luigi Bianchi')}")   # ora funziona