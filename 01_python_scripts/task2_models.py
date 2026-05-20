"""
Parte 1: Record e Dataset
Creazione:
    - Classe Bicicletta — pattern Record
    - Classe FlottaBici — pattern Dataset
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
                 km_percorsi:       float,      # formato: 0.00 (km)
                 disponibile:       bool,):     # formato: True/False
        
        # --[validazione id_bici, prima dell'assegnazione]--
        valida_id_bici(id_bici)

        self.id_bici =              id_bici
        self.tipo =                 tipo
        self.stazione_corrente =    stazione_corrente
        self.km_percorsi =          km_percorsi
        self.disponibile =          disponibile
        self.utente_corrente =      None        # popolato da noleggia(), svuotato da restituisci()
    
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
                    km_aggiunta:    float   # formato: 0.00 (km)
                    ) -> None:
        
        # --[verifica se stazione esiste, altrimenti solleva 'ValueError']--
        if not stazione or not stazione.strip():
            raise ValueError(f"Stazione {stazione} non presente")
        
        # --[verifica se km_aggiunta è positivo, altrimenti solleva 'ValueError']--
        if km_aggiunta < 0:
            raise ValueError(f"Km inseriti '{km_aggiunta}' non validi, inserire un numero positivo")
        
        # --[aggiorna posizione | somma km_aggiunta | imposta disponibile = True | reset di utente_corrente]--
        self.stazione_corrente =    stazione
        self.km_percorsi +=         km_aggiunta
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