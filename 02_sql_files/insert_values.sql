-- [Dati: stazioni] --
-- 5 stazioni per città → 15 stazioni totali

INSERT INTO stazioni VALUES
-- Milano
('ST-MI-01', 'Cadorna',       'Milano',  20, 45.4654, 9.1859),
('ST-MI-02', 'Loreto',        'Milano',  15, 45.4815, 9.2240),
('ST-MI-03', 'Centrale',      'Milano',  25, 45.4862, 9.2045),
('ST-MI-04', 'Duomo',         'Milano',  30, 45.4641, 9.1919),
('ST-MI-05', 'Garibaldi',     'Milano',  18, 45.4847, 9.1870),
-- Roma
('ST-RM-01', 'Termini',       'Roma',    25, 41.9009, 12.5010),
('ST-RM-02', 'Colosseo',      'Roma',    20, 41.8902, 12.4922),
('ST-RM-03', 'Trastevere',    'Roma',    15, 41.8878, 12.4695),
('ST-RM-04', 'Prati',         'Roma',    18, 41.9082, 12.4607),
('ST-RM-05', 'Testaccio',     'Roma',    12, 41.8769, 12.4762),
-- Torino
('ST-TO-01', 'Porta Nuova',   'Torino',  20, 45.0607, 7.6757),
('ST-TO-02', 'Porta Susa',    'Torino',  18, 45.0707, 7.6658),
('ST-TO-03', 'Piazza Castello','Torino', 25, 45.0735, 7.6862),
('ST-TO-04', 'Lingotto',      'Torino',  15, 45.0337, 7.6640),
('ST-TO-05', 'Mirafiori',     'Torino',  10, 45.0102, 7.6380);

-- [Dati: biciclette] --
-- 10 bici per città → 30 biciclette totali (6 elettriche + 4 classiche per città)
 
INSERT INTO biciclette VALUES
-- Milano
('MI-001', 'classica',  'Milano', 'Cadorna',   120.5),
('MI-002', 'classica',  'Milano', 'Loreto',     85.0),
('MI-003', 'classica',  'Milano', 'Centrale',  200.0),
('MI-004', 'classica',  'Milano', 'Duomo',      60.0),
('MI-005', 'elettrica', 'Milano', 'Garibaldi', 340.0),
('MI-006', 'elettrica', 'Milano', 'Cadorna',   210.5),
('MI-007', 'elettrica', 'Milano', 'Loreto',    180.0),
('MI-008', 'elettrica', 'Milano', 'Centrale',  420.0),
('MI-009', 'elettrica', 'Milano', 'Duomo',     155.0),
('MI-010', 'elettrica', 'Milano', 'Garibaldi', 290.0),
-- Roma
('RM-001', 'classica',  'Roma',   'Termini',   310.0),
('RM-002', 'classica',  'Roma',   'Colosseo',  140.0),
('RM-003', 'classica',  'Roma',   'Trastevere', 95.0),
('RM-004', 'classica',  'Roma',   'Prati',      75.0),
('RM-005', 'elettrica', 'Roma',   'Testaccio', 260.0),
('RM-006', 'elettrica', 'Roma',   'Termini',   390.0),
('RM-007', 'elettrica', 'Roma',   'Colosseo',  175.0),
('RM-008', 'elettrica', 'Roma',   'Trastevere',220.0),
('RM-009', 'elettrica', 'Roma',   'Prati',     130.0),
('RM-010', 'elettrica', 'Roma',   'Testaccio', 480.0),
-- Torino
('TO-001', 'classica',  'Torino', 'Porta Nuova', 90.0),
('TO-002', 'classica',  'Torino', 'Porta Susa',  55.0),
('TO-003', 'classica',  'Torino', 'Piazza Castello', 110.0),
('TO-004', 'classica',  'Torino', 'Lingotto',    40.0),
('TO-005', 'elettrica', 'Torino', 'Mirafiori',  200.0),
('TO-006', 'elettrica', 'Torino', 'Porta Nuova',310.0),
('TO-007', 'elettrica', 'Torino', 'Porta Susa', 150.0),
('TO-008', 'elettrica', 'Torino', 'Piazza Castello', 275.0),
('TO-009', 'elettrica', 'Torino', 'Lingotto',   190.0),
('TO-010', 'elettrica', 'Torino', 'Mirafiori',  360.0);
 
 
-- [Dati: utenti] --
-- 10 utenti per città → 30 utenti totali (mix Base/Premium)
 
INSERT INTO utenti VALUES
-- Milano
('U-MI-01', 'Luca Rossi',      'Milano', 'Premium', '2024-01-10'),
('U-MI-02', 'Sara Bianchi',    'Milano', 'Base',    '2024-03-22'),
('U-MI-03', 'Marco Verdi',     'Milano', 'Premium', '2023-11-05'),
('U-MI-04', 'Anna Neri',       'Milano', 'Base',    '2024-06-18'),
('U-MI-05', 'Paolo Ferrari',   'Milano', 'Premium', '2023-08-30'),
('U-MI-06', 'Giulia Russo',    'Milano', 'Base',    '2024-02-14'),
('U-MI-07', 'Matteo Esposito', 'Milano', 'Premium', '2023-12-01'),
('U-MI-08', 'Chiara Romano',   'Milano', 'Base',    '2024-04-09'),
('U-MI-09', 'Davide Greco',    'Milano', 'Premium', '2024-01-25'),
('U-MI-10', 'Elena Marino',    'Milano', 'Base',    '2024-05-03'),
-- Roma
('U-RM-01', 'Alessio Conti',   'Roma',   'Premium', '2023-09-12'),
('U-RM-02', 'Francesca Ricci', 'Roma',   'Base',    '2024-07-01'),
('U-RM-03', 'Simone Lombardi', 'Roma',   'Premium', '2023-10-20'),
('U-RM-04', 'Valentina Costa', 'Roma',   'Base',    '2024-02-28'),
('U-RM-05', 'Roberto Gallo',   'Roma',   'Premium', '2023-07-15'),
('U-RM-06', 'Monica Bruno',    'Roma',   'Base',    '2024-08-05'),
('U-RM-07', 'Stefano Martini', 'Roma',   'Premium', '2024-03-11'),
('U-RM-08', 'Laura Serra',     'Roma',   'Base',    '2024-01-30'),
('U-RM-09', 'Andrea Fontana',  'Roma',   'Premium', '2023-11-22'),
('U-RM-10', 'Paola Caruso',    'Roma',   'Base',    '2024-06-07'),
-- Torino
('U-TO-01', 'Giorgio Fiore',   'Torino', 'Premium', '2023-12-15'),
('U-TO-02', 'Silvia Marini',   'Torino', 'Base',    '2024-04-20'),
('U-TO-03', 'Fabio Santoro',   'Torino', 'Premium', '2024-02-08'),
('U-TO-04', 'Cristina Vitale', 'Torino', 'Base',    '2024-07-14'),
('U-TO-05', 'Enrico De Luca',  'Torino', 'Premium', '2023-08-03'),
('U-TO-06', 'Marta Galli',     'Torino', 'Base',    '2024-05-25'),
('U-TO-07', 'Nicola Ferri',    'Torino', 'Premium', '2023-10-10'),
('U-TO-08', 'Teresa Monti',    'Torino', 'Base',    '2024-03-17'),
('U-TO-09', 'Claudio Barbieri','Torino', 'Premium', '2024-01-05'),
('U-TO-10', 'Irene Cattaneo',  'Torino', 'Base',    '2024-06-30');
 
 
-- [Dati: corse] --
/* 	~110 corse distribuite tra le tre città e vari mesi
	Date: marzo–maggio 2026 con concentrazione in aprile (per D4)
	Utenti Premium con 10+ corse per testare D5 */
 
INSERT INTO corse VALUES
-- Milano — corse utenti Premium (U-MI-01 ne ha 12, U-MI-03 ne ha 11)
('C-001', 'MI-001', 'U-MI-01', 'Cadorna',   'Loreto',    '2026-04-02', 22, 3.80),
('C-002', 'MI-005', 'U-MI-01', 'Loreto',    'Centrale',  '2026-04-05', 35, 6.20),
('C-003', 'MI-006', 'U-MI-01', 'Centrale',  'Duomo',     '2026-04-08', 18, 3.10),
('C-004', 'MI-001', 'U-MI-01', 'Duomo',     'Garibaldi', '2026-04-10', 28, 4.90),
('C-005', 'MI-007', 'U-MI-01', 'Garibaldi', 'Cadorna',   '2026-04-12', 42, 7.50),
('C-006', 'MI-002', 'U-MI-01', 'Cadorna',   'Duomo',     '2026-04-15', 15, 2.70),
('C-007', 'MI-008', 'U-MI-01', 'Loreto',    'Garibaldi', '2026-04-18', 55, 9.80),
('C-008', 'MI-003', 'U-MI-01', 'Centrale',  'Cadorna',   '2026-04-20', 12, 2.10),
('C-009', 'MI-009', 'U-MI-01', 'Duomo',     'Loreto',    '2026-04-22', 33, 5.90),
('C-010', 'MI-005', 'U-MI-01', 'Garibaldi', 'Centrale',  '2026-04-25', 48, 8.60),
('C-011', 'MI-001', 'U-MI-01', 'Cadorna',   'Garibaldi', '2026-05-02', 20, 3.50),
('C-012', 'MI-006', 'U-MI-01', 'Loreto',    'Duomo',     '2026-05-08', 38, 6.80),
 
('C-013', 'MI-002', 'U-MI-03', 'Cadorna',   'Loreto',    '2026-03-10', 25, 4.40),
('C-014', 'MI-007', 'U-MI-03', 'Loreto',    'Centrale',  '2026-03-15', 40, 7.10),
('C-015', 'MI-003', 'U-MI-03', 'Centrale',  'Duomo',     '2026-03-20', 17, 3.00),
('C-016', 'MI-008', 'U-MI-03', 'Duomo',     'Cadorna',   '2026-04-03', 52, 9.30),
('C-017', 'MI-004', 'U-MI-03', 'Garibaldi', 'Loreto',    '2026-04-07', 10, 1.80),
('C-018', 'MI-009', 'U-MI-03', 'Cadorna',   'Centrale',  '2026-04-11', 30, 5.40),
('C-019', 'MI-010', 'U-MI-03', 'Loreto',    'Garibaldi', '2026-04-14', 45, 8.00),
('C-020', 'MI-001', 'U-MI-03', 'Centrale',  'Duomo',     '2026-04-17', 22, 3.90),
('C-021', 'MI-005', 'U-MI-03', 'Duomo',     'Cadorna',   '2026-04-21', 60, 10.70),
('C-022', 'MI-006', 'U-MI-03', 'Garibaldi', 'Loreto',    '2026-04-24', 14, 2.50),
('C-023', 'MI-007', 'U-MI-03', 'Cadorna',   'Garibaldi', '2026-05-05', 36, 6.40),
 
-- Milano — corse utenti Base
('C-024', 'MI-002', 'U-MI-02', 'Loreto',    'Cadorna',   '2026-04-04', 19, 3.30),
('C-025', 'MI-004', 'U-MI-04', 'Duomo',     'Centrale',  '2026-04-06', 27, 4.80),
('C-026', 'MI-008', 'U-MI-06', 'Garibaldi', 'Loreto',    '2026-04-09', 8,  1.40),
('C-027', 'MI-003', 'U-MI-08', 'Centrale',  'Garibaldi', '2026-04-13', 44, 7.90),
('C-028', 'MI-010', 'U-MI-10', 'Loreto',    'Duomo',     '2026-04-16', 31, 5.60),
('C-029', 'MI-001', 'U-MI-02', 'Cadorna',   'Loreto',    '2026-04-19', 23, 4.10),
('C-030', 'MI-009', 'U-MI-04', 'Duomo',     'Garibaldi', '2026-04-23', 50, 8.90),
('C-031', 'MI-004', 'U-MI-06', 'Garibaldi', 'Cadorna',   '2026-04-26', 16, 2.90),
('C-032', 'MI-002', 'U-MI-08', 'Loreto',    'Centrale',  '2026-04-28', 37, 6.60),
('C-033', 'MI-010', 'U-MI-10', 'Centrale',  'Loreto',    '2026-05-03', 29, 5.20),
 
-- Milano — utente Premium U-MI-05 (10 corse esatte)
('C-034', 'MI-005', 'U-MI-05', 'Garibaldi', 'Duomo',     '2026-04-01', 26, 4.60),
('C-035', 'MI-006', 'U-MI-05', 'Cadorna',   'Centrale',  '2026-04-04', 41, 7.30),
('C-036', 'MI-007', 'U-MI-05', 'Loreto',    'Garibaldi', '2026-04-08', 13, 2.30),
('C-037', 'MI-008', 'U-MI-05', 'Centrale',  'Loreto',    '2026-04-12', 57, 10.20),
('C-038', 'MI-009', 'U-MI-05', 'Duomo',     'Cadorna',   '2026-04-16', 20, 3.60),
('C-039', 'MI-010', 'U-MI-05', 'Garibaldi', 'Loreto',    '2026-04-20', 34, 6.10),
('C-040', 'MI-005', 'U-MI-05', 'Cadorna',   'Garibaldi', '2026-04-24', 47, 8.40),
('C-041', 'MI-006', 'U-MI-05', 'Loreto',    'Centrale',  '2026-04-28', 11, 2.00),
('C-042', 'MI-007', 'U-MI-05', 'Centrale',  'Duomo',     '2026-05-06', 39, 7.00),
('C-043', 'MI-008', 'U-MI-05', 'Duomo',     'Loreto',    '2026-05-10', 24, 4.30),
 
-- Roma — corse utenti Premium (U-RM-01 ha 11 corse, U-RM-03 ha 10)
('C-044', 'RM-001', 'U-RM-01', 'Termini',   'Colosseo',  '2026-04-01', 30, 5.40),
('C-045', 'RM-005', 'U-RM-01', 'Colosseo',  'Trastevere','2026-04-04', 43, 7.70),
('C-046', 'RM-006', 'U-RM-01', 'Trastevere','Prati',     '2026-04-07', 19, 3.40),
('C-047', 'RM-002', 'U-RM-01', 'Prati',     'Testaccio', '2026-04-10', 55, 9.90),
('C-048', 'RM-007', 'U-RM-01', 'Testaccio', 'Termini',   '2026-04-13', 14, 2.50),
('C-049', 'RM-008', 'U-RM-01', 'Termini',   'Trastevere','2026-04-16', 38, 6.80),
('C-050', 'RM-003', 'U-RM-01', 'Colosseo',  'Prati',     '2026-04-19', 26, 4.70),
('C-051', 'RM-009', 'U-RM-01', 'Trastevere','Testaccio', '2026-04-22', 50, 8.90),
('C-052', 'RM-010', 'U-RM-01', 'Prati',     'Colosseo',  '2026-04-25', 22, 3.90),
('C-053', 'RM-004', 'U-RM-01', 'Testaccio', 'Termini',   '2026-04-28', 60, 10.80),
('C-054', 'RM-005', 'U-RM-01', 'Termini',   'Prati',     '2026-05-04', 33, 5.90),
 
('C-055', 'RM-002', 'U-RM-03', 'Colosseo',  'Termini',   '2026-03-05', 28, 5.00),
('C-056', 'RM-006', 'U-RM-03', 'Termini',   'Testaccio', '2026-03-12', 45, 8.10),
('C-057', 'RM-007', 'U-RM-03', 'Trastevere','Colosseo',  '2026-03-19', 17, 3.00),
('C-058', 'RM-008', 'U-RM-03', 'Prati',     'Termini',   '2026-04-02', 52, 9.30),
('C-059', 'RM-003', 'U-RM-03', 'Testaccio', 'Trastevere','2026-04-06', 11, 2.00),
('C-060', 'RM-009', 'U-RM-03', 'Termini',   'Colosseo',  '2026-04-10', 36, 6.40),
('C-061', 'RM-010', 'U-RM-03', 'Colosseo',  'Prati',     '2026-04-14', 48, 8.60),
('C-062', 'RM-004', 'U-RM-03', 'Trastevere','Testaccio', '2026-04-18', 21, 3.70),
('C-063', 'RM-005', 'U-RM-03', 'Prati',     'Termini',   '2026-04-22', 40, 7.20),
('C-064', 'RM-006', 'U-RM-03', 'Testaccio', 'Colosseo',  '2026-04-26', 15, 2.70),
 
-- Roma — corse utenti Base
('C-065', 'RM-001', 'U-RM-02', 'Termini',   'Prati',     '2026-04-03', 24, 4.30),
('C-066', 'RM-003', 'U-RM-04', 'Trastevere','Colosseo',  '2026-04-08', 37, 6.60),
('C-067', 'RM-007', 'U-RM-06', 'Colosseo',  'Testaccio', '2026-04-11', 9,  1.60),
('C-068', 'RM-002', 'U-RM-08', 'Prati',     'Trastevere','2026-04-15', 44, 7.90),
('C-069', 'RM-009', 'U-RM-10', 'Testaccio', 'Termini',   '2026-04-20', 31, 5.60),
('C-070', 'RM-004', 'U-RM-02', 'Termini',   'Colosseo',  '2026-04-24', 18, 3.20),
('C-071', 'RM-010', 'U-RM-04', 'Colosseo',  'Trastevere','2026-04-27', 53, 9.50),
('C-072', 'RM-001', 'U-RM-06', 'Prati',     'Testaccio', '2026-05-01', 27, 4.90),
('C-073', 'RM-008', 'U-RM-08', 'Trastevere','Termini',   '2026-05-07', 42, 7.50),
 
-- Torino — corse utenti Premium (U-TO-01 ha 10 corse, U-TO-03 ha 10)
('C-074', 'TO-001', 'U-TO-01', 'Porta Nuova',    'Porta Susa',      '2026-04-01', 20, 3.60),
('C-075', 'TO-005', 'U-TO-01', 'Porta Susa',     'Piazza Castello', '2026-04-04', 35, 6.30),
('C-076', 'TO-006', 'U-TO-01', 'Piazza Castello','Lingotto',        '2026-04-07', 48, 8.60),
('C-077', 'TO-002', 'U-TO-01', 'Lingotto',       'Mirafiori',       '2026-04-10', 15, 2.70),
('C-078', 'TO-007', 'U-TO-01', 'Mirafiori',      'Porta Nuova',     '2026-04-13', 58, 10.40),
('C-079', 'TO-008', 'U-TO-01', 'Porta Nuova',    'Piazza Castello', '2026-04-17', 26, 4.70),
('C-080', 'TO-003', 'U-TO-01', 'Porta Susa',     'Lingotto',        '2026-04-21', 40, 7.20),
('C-081', 'TO-009', 'U-TO-01', 'Piazza Castello','Mirafiori',       '2026-04-25', 12, 2.10),
('C-082', 'TO-010', 'U-TO-01', 'Lingotto',       'Porta Nuova',     '2026-04-28', 33, 5.90),
('C-083', 'TO-004', 'U-TO-01', 'Mirafiori',      'Porta Susa',      '2026-05-05', 22, 3.90),
 
('C-084', 'TO-002', 'U-TO-03', 'Porta Susa',     'Porta Nuova',     '2026-03-08', 30, 5.40),
('C-085', 'TO-006', 'U-TO-03', 'Porta Nuova',    'Lingotto',        '2026-03-15', 55, 9.90),
('C-086', 'TO-007', 'U-TO-03', 'Piazza Castello','Mirafiori',       '2026-03-22', 18, 3.20),
('C-087', 'TO-008', 'U-TO-03', 'Lingotto',       'Porta Susa',      '2026-04-03', 42, 7.50),
('C-088', 'TO-009', 'U-TO-03', 'Mirafiori',      'Piazza Castello', '2026-04-09', 10, 1.80),
('C-089', 'TO-010', 'U-TO-03', 'Porta Nuova',    'Porta Susa',      '2026-04-13', 37, 6.60),
('C-090', 'TO-001', 'U-TO-03', 'Porta Susa',     'Lingotto',        '2026-04-17', 50, 8.90),
('C-091', 'TO-005', 'U-TO-03', 'Piazza Castello','Mirafiori',       '2026-04-21', 24, 4.30),
('C-092', 'TO-003', 'U-TO-03', 'Lingotto',       'Porta Nuova',     '2026-04-25', 44, 7.90),
('C-093', 'TO-006', 'U-TO-03', 'Mirafiori',      'Porta Susa',      '2026-04-29', 16, 2.90),
 
-- Torino — corse utenti Base
('C-094', 'TO-001', 'U-TO-02', 'Porta Nuova',    'Mirafiori',       '2026-04-05', 28, 5.00),
('C-095', 'TO-004', 'U-TO-04', 'Lingotto',       'Piazza Castello', '2026-04-09', 39, 7.00),
('C-096', 'TO-008', 'U-TO-06', 'Porta Susa',     'Lingotto',        '2026-04-12', 8,  1.40),
('C-097', 'TO-003', 'U-TO-08', 'Piazza Castello','Porta Nuova',     '2026-04-16', 46, 8.30),
('C-098', 'TO-009', 'U-TO-10', 'Mirafiori',      'Porta Susa',      '2026-04-20', 21, 3.80),
('C-099', 'TO-002', 'U-TO-02', 'Porta Nuova',    'Piazza Castello', '2026-04-23', 34, 6.10),
('C-100', 'TO-010', 'U-TO-04', 'Porta Susa',     'Mirafiori',       '2026-04-27', 57, 10.20),
('C-101', 'TO-004', 'U-TO-06', 'Piazza Castello','Lingotto',        '2026-05-02', 13, 2.30),
('C-102', 'TO-007', 'U-TO-08', 'Lingotto',       'Porta Nuova',     '2026-05-09', 29, 5.20),
('C-103', 'TO-005', 'U-TO-10', 'Mirafiori',      'Piazza Castello', '2026-05-12', 43, 7.70),
 
-- Corse extra per superare quota arrivi stazioni Milano in aprile (D4)
('C-104', 'MI-003', 'U-MI-07', 'Cadorna',   'Loreto',    '2026-04-05', 32, 5.70),
('C-105', 'MI-004', 'U-MI-09', 'Loreto',    'Duomo',     '2026-04-09', 46, 8.20),
('C-106', 'MI-010', 'U-MI-07', 'Garibaldi', 'Cadorna',   '2026-04-12', 21, 3.70),
('C-107', 'MI-001', 'U-MI-09', 'Centrale',  'Loreto',    '2026-04-15', 38, 6.80),
('C-108', 'MI-005', 'U-MI-07', 'Duomo',     'Garibaldi', '2026-04-18', 55, 9.80),
('C-109', 'MI-006', 'U-MI-09', 'Loreto',    'Cadorna',   '2026-04-21', 17, 3.00),
('C-110', 'MI-007', 'U-MI-07', 'Cadorna',   'Centrale',  '2026-04-24', 42, 7.50),
('C-111', 'MI-008', 'U-MI-09', 'Garibaldi', 'Duomo',     '2026-04-27', 29, 5.20);