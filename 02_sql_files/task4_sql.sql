/* 	D1 — Tutte le corse a Milano ordinate per data decrescente. 
	     Mostra: id_corsa, id_bici, data_corsa, durata_minuti
	---------------------------------------------------------
	Spiegazione: filtra le corse in cui la bici appartiene a Milano usando una
	JOIN sulla tabella biciclette. ORDER BY data_corsa DESC mette le corse
	più recenti in cima. */
 
SELECT
    c.id_corsa,
    c.id_bici,
    c.data_corsa,
    c.durata_minuti
FROM corse 		AS c
JOIN biciclette AS b	ON c.id_bici = b.id_bici
WHERE b.citta = 'Milano'
ORDER BY c.data_corsa DESC;

/*	D2 — Quante bici elettriche per ogni città? 
		 Ordina dalla città con più bici a quella con meno.
	-------------------------------------------------------
    Spiegazione: filtra solo le bici elettriche con WHERE, poi raggruppa per
	città con GROUP BY e conta con COUNT(id_bici). ORDER BY DESC mostra prima
	la città con la flotta elettrica più grande. */
 
SELECT
    citta,
    COUNT(id_bici)	AS n_bici_elettriche
FROM biciclette
WHERE tipo = 'elettrica'
GROUP BY citta
ORDER BY n_bici_elettriche DESC;

/*	D3 — Durata media, massima e minima per tipo di bicicletta. 
    (JOIN richiesto)
    ----------------------------------------------------------
    Spiegazione: il JOIN collega ogni corsa al tipo della bici usata.
	GROUP BY b.tipo calcola le statistiche separatamente per 'classica' ed
	'elettrica'. ROUND arrotonda la media a 1 decimale per leggibilità.*/
    
SELECT
    b.tipo,
    ROUND(AVG(c.durata_minuti), 1)	AS durata_media,
    MAX(c.durata_minuti)           	AS durata_max,
    MIN(c.durata_minuti)           	AS durata_min
FROM corse 		AS c
JOIN biciclette	AS b	ON c.id_bici = b.id_bici
GROUP BY b.tipo;

/*	D4 — Stazioni di Milano con più di 50 arrivi in aprile 2026.
	     Ordina per conteggio decrescente.
	-----------------------------------------------------------
    Spiegazione: filtra le corse con WHERE stazione_arrivo in Milano
    (JOIN su stazioni) e data in aprile 2026 con LIKE '2026-04-%'. 
    GROUP BY stazione_arrivo aggrega per stazione. 
    HAVING filtra n_arrivi dopo l'aggregazione */

SELECT
    c.stazione_arrivo,
    COUNT(c.id_corsa)	AS n_arrivi
FROM corse		AS c
JOIN stazioni	AS s	ON c.stazione_arrivo = s.nome
WHERE s.citta = 'Milano'	AND	c.data_corsa LIKE '2026-04-%'
GROUP BY c.stazione_arrivo
HAVING n_arrivi > 5 		-- soglia abbassata a 5 per il dataset di prova (~110 record)
                            -- nella realtà con dati reali la soglia sarebbe 50
ORDER BY n_arrivi DESC;

/*	D5 — Utenti "Premium" con almeno 10 corse: 
	     mostra numero corse totali e km totali. (JOIN richiesto)
	-------------------------------------------------------------
    Spiegazione: il JOIN collega ogni corsa al suo utente. 
    WHERE filtra solo i Premium. 
    GROUP BY u.id_utente aggrega per utente. 
    HAVING filtra gli utenti con n_corse_totali >= 10 corse calcolato 
    dopo il raggruppamento.*/

SELECT
    u.id_utente,
    u.nome,
    COUNT(c.id_corsa)              AS n_corse_totali,
    ROUND(SUM(c.km_percorsi), 1)   AS km_totali
FROM corse		AS c
JOIN utenti 	AS u	ON c.id_utente = u.id_utente
WHERE u.tipo_abbonamento = 'Premium'
GROUP BY u.id_utente, u.nome
HAVING n_corse_totali >= 10
ORDER BY km_totali DESC;

/*	D6 — Spiega a parole cosa fa questa query e 
		 quale informazione di business produce: */

SELECT
    s.nome AS stazione,
    s.citta,
    COUNT(c_in.id_corsa)  AS arrivi,
    COUNT(c_out.id_corsa) AS partenze,
    COUNT(c_in.id_corsa) - COUNT(c_out.id_corsa) AS bilancio
FROM stazioni s
LEFT JOIN corse c_in  ON s.nome = c_in.stazione_arrivo
LEFT JOIN corse c_out ON s.nome = c_out.stazione_partenza
GROUP BY s.nome, s.citta
ORDER BY bilancio DESC;

/*	Spiegazione: la query calcola il bilancio di flusso delle
	bibi raggruppando per stazione e citta. serve per monitorare
    squilibri nel flusso di bici per cui ci possono essere
    destinazioni 'popolari' in cui le bici si accumulano e
    partenze 'centrali' (es stazione treno) da cui partono
    molte più bici. il bilancio permette di anticipare il 
    problema logistico di stazioni 'vuote' o 'sovraaffolate'
    pianificando dei trasferimenti regolari per ribilanciare
    le quantità di bici in ogni stazione.*/