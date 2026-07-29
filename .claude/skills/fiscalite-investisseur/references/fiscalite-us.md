# Fiscalité américaine et situations franco-américaines

⚠️ Chiffres indexés chaque année par l'IRS — vérifier en ligne l'année concernée (irs.gov).

## Federal income tax (repères 2025, indicatif)

- 7 tranches : 10 / 12 / 22 / 24 / 32 / 35 / 37 %
- Standard deduction : ~15 000 $ (single), ~30 000 $ (married filing jointly)
- NIIT (net investment income tax) : +3,8 % sur les revenus du capital au-delà de 200 k$ (single) / 250 k$ (MFJ)

## Capital gains

| Type | Détention | Taux |
|---|---|---|
| Short-term | ≤ 1 an | Barème ordinaire (jusqu'à 37 %) |
| Long-term | > 1 an | 0 / 15 / 20 % selon revenu (+ NIIT 3,8 % le cas échéant) |
| Qualified dividends | Holding period respecté | Taux long-term |
| Ordinary dividends | — | Barème ordinaire |

- **Wash sale rule (IRC §1091)** : perte refusée si rachat d'un titre substantially identical dans la fenêtre ±30 jours ; la perte refusée s'ajoute au cost basis du rachat. S'applique sur l'ensemble des comptes du foyer, IRA inclus (perte définitivement perdue si rachat en IRA)
- **Cost basis** : FIFO par défaut, specific identification possible si documentée avant la vente — levier majeur d'optimisation
- **Pertes nettes** : compensation gains puis 3 000 $/an max sur le revenu ordinaire, report illimité
- **Formulaires** : ventes détaillées sur Form 8949 → synthèse Schedule D → 1040 ; les courtiers émettent un 1099-B (vérifier les cost basis « non couverts »)

## Retraite et enveloppes (plafonds 2025, indexés)

- 401(k) : 23 500 $ (+7 500 $ catch-up 50+) ; Traditional ou Roth
- IRA : 7 000 $ (+1 000 $ catch-up) ; déductibilité et accès Roth soumis à des limites de revenus (backdoor Roth : conversion après contribution non déductible — attention à la pro-rata rule)
- HSA : ~4 300 $ individuel / ~8 550 $ famille (éligibilité HDHP)
- RMD : distributions minimales obligatoires à partir de 73 ans (Traditional)

## Convention fiscale France–États-Unis (1994 modifiée)

- **Dividendes** : retenue à la source limitée à 15 % (W-8BEN pour un résident FR chez un courtier US) ; côté FR : crédit d'impôt égal à l'impôt étranger (case 2AB/8VL), le PFU s'applique sur le brut
- **Intérêts** : imposition exclusive dans l'État de résidence (0 % de retenue US en général)
- **Plus-values mobilières** : imposables uniquement dans l'État de résidence
- **Immobilier** : imposable dans l'État de situation (FIRPTA côté US pour les non-résidents : retenue 15 % sur le prix de vente)
- **Élimination de la double imposition côté FR** : crédit d'impôt égal à l'impôt français (revenus US exonérés mais pris en compte pour le taux effectif) ou égal à l'impôt US selon la catégorie

## Pièges des situations mixtes

- **US person en France** (citoyen, green card, substantial presence) : imposition mondiale US quelle que soit la résidence → déclaration 1040 annuelle + FBAR (FinCEN 114, comptes étrangers > 10 k$ agrégés) + Form 8938 (FATCA)
- **PFIC** : les fonds et ETF non-US (donc UCITS) sont des Passive Foreign Investment Companies → fiscalité punitive et Form 8621 par fonds — une US person en France doit éviter les ETF européens et l'assurance-vie en unités de compte (souvent traitée comme PFIC wrapper)
- **Foreign Earned Income Exclusion (Form 2555)** : ~130 k$ de salaires exclus, OU foreign tax credit (Form 1116) — souvent plus favorable en France (impôt FR > impôt US)
- **Départ de France vers les US** : exit tax française possible (art. 167 bis) si participations > 800 k€ ou > 50 % d'une société — sursis de paiement à demander
- **Impatriés en France (155 B)** : exonérations partielles (prime d'impatriation, 50 % des RCM étrangers) jusqu'à 8 ans — vérifier l'éligibilité
- **Résident FR avec compte chez un courtier US** : formulaire 3916 obligatoire (amende 1 500 €/compte non déclaré), revenus à reporter sur la 2047

## State taxes

- États sans impôt sur le revenu : FL, TX, WA, NV, TN, SD, WY, AK (NH sur salaires)
- Résidence fiscale d'État : critères propres (domicile, 183 jours…) — la Californie et New York sont agressives sur les départs
