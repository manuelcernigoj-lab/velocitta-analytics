"""
Creazione della funzione calcola_durata_minuti(ora_inizio: str, ora_fine: str) -> int
    - Formato input: "HH:MM"
    - Solleva ValueError se ora_fine è precedente a ora_inizio
"""

def calcola_durata_minuti(ora_inizio: str, ora_fine: str) -> int:
    """
    Calcola la durata in minuti tra due orari in formato 'HH:MM'.

    Parameters
    ----------
    ora_inizio : str
        Orario di inizio, formato 'HH:MM' (es. '08:30').
    ora_fine : str
        Orario di fine, formato 'HH:MM' (es. '09:15').

    Returns
    -------
    int
        Durata in minuti interi tra i due orari.

    Raises
    ------
    ValueError
        Se ora_fine è precedente o uguale a ora_inizio.

    Examples
    --------
    >>> calcola_durata_minuti('08:30', '09:15')
    45
    >>> calcola_durata_minuti('23:00', '08:00')
    ValueError: ora_fine deve essere successiva a ora_inizio
    """
    
    # --[funzione interna per validare che l'orario sia nel formato corretto]--
    def _valida_orario(orario: str, nome: str) -> tuple[int, int]:
        """
        Valida formato e valori di un orario 'HH:MM', restituisce (ore, minuti).
        """

        try:
            hh, mm = orario.split(":")
            hh, mm = int(hh), int(mm)
        except ValueError:
            raise ValueError(f"{nome} non è in formato valido 'HH:MM': '{orario}'")
            # ↘ il parametro nome serve a dare messaggi di errore precisi 
            #   su quale dei due orari è sbagliato.

        if not (0 <= hh <= 23):
            raise ValueError(f"{nome}: ore fuori range (0-23), ricevuto {hh}")
        if not (0 <= mm <= 59):
            raise ValueError(f"{nome}: minuti fuori range (0-59), ricevuto {mm}")
        
        return hh, mm

    # --[salvataggio di hh e mm di inizio e fine in delle variabili]--
    hh_i, mm_i = _valida_orario(ora_inizio, "ora_inizio")
    hh_f, mm_f = _valida_orario(ora_fine,   "ora_fine")

    # --[calcolo dei totali di inizio e fine in minuti per semplificare la verifica]--
    inizio_tot = hh_i * 60 + mm_i
    fine_tot   = hh_f * 60 + mm_f

    # --[solleva 'ValueError' se ora_fine è precedente a ora_inizio]--
    if fine_tot <= inizio_tot:
        raise ValueError(f"ora_fine '{ora_fine}' deve essere successiva a ora_inizio '{ora_inizio}'")

    return fine_tot - inizio_tot

"""
Creazione della funzione classifica_corsa(durata_minuti: int) -> str
    - "breve" se < 15 min, "media" se 15-45 min, "lunga" se > 45 min
"""

def classifica_corsa(durata_minuti: int) -> str:
    """
    Classifica una corsa in base alla sua durata in minuti.

    Parameters
    ----------
    durata_minuti : int
        Durata della corsa in minuti interi. Deve essere > 0.

    Returns
    -------
    str
        Categoria della corsa:
        - 'breve'  : durata < 15 min
        - 'media'  : 15 <= durata <= 45 min
        - 'lunga'  : durata > 45 min

    Raises
    ------
    ValueError
        Se durata_minuti è <= 0.

    Examples
    --------
    >>> classifica_corsa(10)
    'breve'
    >>> classifica_corsa(30)
    'media'
    >>> classifica_corsa(60)
    'lunga'
    """

    # --[classificazione tramite condizioni if/else]--
    if durata_minuti < 0:
        raise ValueError(f"durata_minuti '{durata_minuti}' deve essere maggiore o uguale a zero'")
        # ↘ controllo sull'inserimento di valori negativi → raise ValueError

    elif durata_minuti < 15:
        return "breve"
    elif durata_minuti <= 45:
        return "media"
    else:
        return "lunga"
    
"""
Creazione della funzione riepilogo_corse(lista_durate: list) -> dict
    - Chiavi restituite: totale, media, max, min, brevi, medie, lunghe
"""

def riepilogo_corse(lista_durate: list) -> dict:
    """
    Calcola statistiche riassuntive su una lista di durate di corse.

    Parameters
    ----------
    lista_durate : list[int]
        Lista di durate in minuti interi. Non deve essere vuota.

    Returns
    -------
    dict
        Dizionario con le seguenti chiavi:
        - 'totale'  : int   — durata totale delle corse
        - 'media'   : float — durata media in minuti
        - 'max'     : int   — durata massima in minuti
        - 'min'     : int   — durata minima in minuti
        - 'brevi'   : int   — numero di corse < 15 min
        - 'medie'   : int   — numero di corse tra 15 e 45 min
        - 'lunghe'  : int   — numero di corse > 45 min

    Raises
    ------
    ValueError
        Se lista_durate è vuota.

    Examples
    --------
    >>> riepilogo_corse([10, 30, 60, 20, 5])
    {
        'totale':   125,
        'media':    25.0,
        'max':      60,
        'min':      5,
        'brevi':    2,
        'medie':    2,
        'lunghe':   1
    }
    """

    # --[validazione input]--
    if not lista_durate:
        raise ValueError("lista_durate non può essere vuota")

    # --[calcolo statistiche per riepilogo]--
    t_durata =  sum(lista_durate)
    media =     sum(lista_durate) / len(lista_durate)
    massimo =   max(lista_durate)
    minimo =    min(lista_durate)

    # per categorizzazione, riutilizzo funzione 'classifica_corsa()'
    brevi, medie, lunghe = 0, 0, 0
    for d in lista_durate:
        cat = classifica_corsa(d)
        if   cat == "breve": brevi  += 1
        elif cat == "media": medie  += 1
        else:                lunghe += 1
    
    # --[creazione dizionario di output]--
    riepilogo = {
        "totale":   t_durata,
        "media":    media,
        "max":      massimo,
        "min":      minimo,
        "brevi":    brevi,
        "medie":    medie,
        "lunghe":   lunghe
        }
    
    return riepilogo