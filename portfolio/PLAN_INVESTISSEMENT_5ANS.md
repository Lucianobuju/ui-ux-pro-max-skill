# Plan d'investissement 5 ans — SPCX + Nasdaq-100 + S&P 500

> Créé le 28/07/2026 · Horizon : juillet 2031 · Objectif : maximiser l'espérance de valeur finale
> ⚠️ Les projections sont des scénarios de travail, pas des promesses. Aucun rendement n'est garanti.

## 1. Architecture (validée par expert-bourse + expert-fiscalite)

| Ligne | Poids cible | Support | Enveloppe | Frais | Pourquoi |
|---|---|---|---|---|---|
| S&P 500 | **65 %** | BNP Easy S&P 500 « ESE » (FR0011550185) | **PEA** | 0,14 % | Cœur diversifié ; exonéré d'IR après 5 ans (PS 18,6 % seuls) |
| Nasdaq-100 | **25 %** | Amundi PEA Nasdaq-100 « PUST » (FR0011871110) | **PEA** | 0,30 % | Surpondération tech assumée |
| SpaceX | **10 %** | Titre vif SPCX (Nasdaq) | **CTO** | courtage | Satellite spéculatif ; flat tax 31,4 % à la sortie |

Chevauchement assumé : ~80 % du Nasdaq-100 est dans le S&P 500 ; SPCX intégrera probablement le Nasdaq-100. Exposition réelle mega-caps tech ≈ 45-50 %.

## 2. Versements (scénario de référence C)

- **5 000 € initial** : indices déployés en 2-3 tranches sur 8 semaines (3 200 € ESE / 1 300 € PUST) ; **500 € SPCX uniquement après le 6 août 2026** (résultats T2 le 4/08, expiration lock-up le 6/08)
- **200 €/mois le 5 du mois** : 130 € ESE / 50 € PUST / 20 € SPCX (fractionné)
- Total investi sur 5 ans : **17 000 €**

Variantes : A (100 €/mois → 85 € ESE + 15 € SPCX, 2 lignes seulement) · B (300 €/mois → 190/80/30)

## 3. Projections à 5 ans (scénario C)

Hypothèses annuelles : S&P 500 2/7/11 % · Nasdaq-100 0/9/14 % · SPCX −15/+10/+30 % (bear/base/bull)

| Scénario | Valeur 2031 | Gain | Performance |
|---|---|---|---|
| 🐻 Bear | 17 080 € | +80 € | +0,5 % |
| ⚖️ Base | **21 810 €** | **+4 810 €** | **+28,3 %** |
| 🚀 Bull | 26 605 € | +9 605 € | +56,5 % |

Évolution annuelle (base) : 5 000 → 7 875 → 10 974 → 14 317 → 17 922 → **21 810 €**

Détail par ligne (base) : ESE 11 050 € investis → 13 814 € (+25 %) · PUST 4 250 → 5 660 € (+33 %) · SPCX 1 700 → 2 336 € (+37 %)

## 4. Règles de discipline (non négociables)

1. DCA le 5 du mois, quoi qu'il arrive — surtout en baisse
2. SPCX plafonné à 12 % : au-delà → écrêtage vers les indices (janvier ou immédiat si dépassement fort)
3. Rééquilibrage annuel en janvier, en privilégiant les arbitrages intra-PEA (zéro friction fiscale)
4. Kill switch SPCX : échecs Starship répétés + marges Starlink dégradées 2 trimestres → sortie ordonnée
5. Jamais : levier, vente panique, suspension du DCA, moyenne à la baisse sur thèse cassée
6. Krach indices > 20 % = opportunité de renforcement si trésorerie, jamais une raison de vendre

## 5. Infrastructure de suivi

| Composant | Rôle |
|---|---|
| `portfolio/portefeuille.json` | Source de vérité : allocation, règles, projections, historique |
| Agent `suivi-portefeuille` | Mesure : cours, perf vs plan, écarts d'allocation, événements — met à jour le JSON |
| Agent `conseiller-portefeuille` | Conseille : objectif unique = valeur 2031 ; niveaux 🟢 silence / 🟡 attention / 🔴 action |
| Routine hebdomadaire (lundi 8h Paris) | Déclenche automatiquement suivi → conseil dans la session |

## 6. Fiscalité (résumé expert-fiscalite)

W-8BEN signé · 3916 par compte étranger chaque année (1 500 € d'amende par oubli) · change EUR/USD noté par lot SPCX · à la revente CTO : flat tax 31,4 % (2026) vs barème — PFU gagnant dès TMI 30 % · PEA : aucune friction tant qu'on ne retire pas, PS 18,6 % sur gains au retrait après 5 ans.

## Calendrier des événements connus

| Date | Événement | Impact |
|---|---|---|
| 04/08/2026 | Résultats T2 SPCX | Premier test public post-IPO |
| 06/08/2026 | Expiration lock-up (~911 M actions) | Pression vendeuse potentielle — point d'entrée planifié |
| Janvier 2027-2031 | Rééquilibrage annuel | Retour à 65/25/10 |
| Mi-2027 | Déblocage titres Musk | Volatilité possible |
| Non daté | Inclusion SPCX au Nasdaq-100 / spin-off Starlink | Catalyseurs haussiers potentiels |
