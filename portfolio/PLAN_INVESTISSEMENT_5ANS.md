# Plan d'investissement 5 ans — MSCI World + Nasdaq-100 + SPCX 🔒 VERROUILLÉ v1.0 (28/07/2026)

> Créé le 28/07/2026 · Horizon : juillet 2031 · Objectif : maximiser l'espérance de valeur finale
> ⚠️ Les projections sont des scénarios de travail, pas des promesses. Aucun rendement n'est garanti.

## 1. Architecture (validée par expert-bourse + expert-fiscalite)

| Ligne | Poids cible | Support | Enveloppe | Frais | Pourquoi |
|---|---|---|---|---|---|
| MSCI World | **65 %** | iShares MSCI World Swap PEA « WPEA » (IE0002XZSHO1) | **PEA** | 0,20 % | Cœur monde (~1 500 valeurs, 23 pays, ~70 % US) ; exonéré d'IR après 5 ans |
| Nasdaq-100 | **25 %** | Amundi PEA Nasdaq-100 « PUST » (FR0011871110) | **PEA** | 0,30 % | Surpondération tech assumée |
| SpaceX | **10 %** | Titre vif SPCX (Nasdaq) | **CTO** | courtage | Satellite spéculatif ; flat tax 31,4 % à la sortie |

WPEA remplace le S&P 500 (déjà ~70 % du World) : vraie diversification (Europe, Japon…) sans ligne supplémentaire. Le Nasdaq-100 reste la surpondération tech assumée ; SPCX intégrera probablement le Nasdaq-100. Part WPEA ~5-6 € : DCA au centime près.

## 2. Versements (plafond : 300 €/mois, décision du 28/07/2026)

DCA pur, aucune injection de capital, jamais plus de 300 € par mois.

- **300 €/mois le 5 du mois** : 195 € WPEA / 75 € PUST / 30 € SPCX (fractionné)
- Ligne SPCX démarrée **après le 6 août 2026** (résultats T2 le 4/08, expiration lock-up le 6/08)
- Total investi sur 5 ans : **18 000 €**

## 3. Projections à 5 ans (300 €/mois)

Hypothèses annuelles : MSCI World 1,5/6,5/10 % · Nasdaq-100 0/9/14 % · SPCX −15/+10/+30 % (bear/base/bull)

| Scénario | Valeur 2031 | Gain | Performance |
|---|---|---|---|
| 🐻 Bear | 17 880 € | −120 € | −0,7 % |
| ⚖️ Base | **21 617 €** | **+3 617 €** | **+20,1 %** |
| 🚀 Bull | 24 933 € | +6 933 € | +38,5 % |

Hypothèses World : 1,5/6,5/10 % (légèrement sous le S&P 500 — le prix de la diversification hors US).
Évolution annuelle (base) : 0 → 3 722 → 7 722 → 12 022 → 16 646 → **21 617 €**

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
| Janvier 2027-2031 | Rééquilibrage annuel | Retour à 65/25/10 (WPEA/PUST/SPCX) |
| Mi-2027 | Déblocage titres Musk | Volatilité possible |
| Non daté | Inclusion SPCX au Nasdaq-100 / spin-off Starlink | Catalyseurs haussiers potentiels |
