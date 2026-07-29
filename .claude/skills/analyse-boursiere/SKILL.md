---
name: analyse-boursiere
description: Méthode d'analyse boursière et de construction de portefeuille — grille d'analyse d'un titre (fondamental + technique), multiples de valorisation par secteur, gestion du risque et position sizing, comparaison des enveloppes FR/US (PEA, CTO, assurance-vie, 401k, IRA). À charger pour analyser une action, un ETF ou construire une allocation.
---

# Analyse boursière — méthode et outils

## Grille d'analyse d'un titre (à suivre dans l'ordre)

1. **Business & moat** : que vend l'entreprise, part de marché, avantage concurrentiel (coûts, marque, effet réseau, switching costs), risque de disruption
2. **Chiffres clés (3-5 ans)** : croissance CA, marges, ROIC vs WACC, FCF, endettement (voir skill `analyse-financiere`)
3. **Valorisation** : multiples vs pairs et vs historique (voir `references/valorisation.md`) ; croiser avec un DCF simplifié
4. **Catalyseurs** : résultats à venir, cycles produits, M&A, réglementation, retour à l'actionnaire (dividendes, buybacks)
5. **Risques** : concentration clients, levier, dilution, gouvernance, risque pays/devise
6. **Scénarios chiffrés** : bull / base / bear avec objectifs de cours et probabilités subjectives
7. **Conclusion** : thèse en 3 phrases + horizon + ce qui invaliderait la thèse (kill switch)

## Lecture technique minimale (timing, pas thèse)

- **Tendance** : au-dessus/en-dessous des moyennes mobiles 50 et 200 jours ; golden/death cross
- **Momentum** : RSI 14 (>70 suracheté, <30 survendu — dans une tendance forte, le RSI peut rester extrême), MACD
- **Volumes** : un breakout sans volume est suspect
- **Régime de marché** : largeur (% de titres au-dessus de leur MM200), VIX, spreads high yield — ne pas ouvrir de position agressive en régime risk-off

## Gestion du risque — règles de base

- **Position sizing** : risque max par position = 1-2 % du portefeuille (distance au stop × taille de position)
- **Concentration** : une ligne = 5 % max du portefeuille pour un particulier diversifié (10 % si forte conviction assumée)
- **Corrélations** : 10 lignes tech ≠ diversification ; croiser secteurs, zones, classes d'actifs
- **Métriques à suivre** : volatilité, max drawdown supportable (le vrai test est psychologique), ratio de Sharpe pour comparer des stratégies
- **DCA vs lump sum** : statistiquement le lump sum gagne ~2 fois sur 3, mais le DCA réduit le risque de regret — choisir selon le profil

## ETF : checklist de sélection

1. Indice répliqué et méthode (physique vs synthétique)
2. TER (frais courants) : viser <0,3 % pour du large cap
3. Encours (>100 M€ pour la pérennité) et liquidité (spread)
4. Domiciliation : UCITS (Irlande/Luxembourg) pour un résident européen — retenue à la source dividendes US réduite à 15 % via l'Irlande ; ETF US inaccessibles en direct (PRIIPs) sauf statut professionnel
5. Capitalisant vs distribuant (interaction avec la fiscalité de l'enveloppe)
6. Éligibilité PEA (indices européens ou réplication synthétique éligible)

## Enveloppes : voir `references/enveloppes.md` pour le comparatif complet FR/US

## Discipline

- Journal de trading : noter thèse, taille, stop, émotion à l'entrée — relire avant chaque nouvelle position
- Jamais de moyenne à la baisse sur une thèse invalidée ; distinguer « le cours baisse » de « la thèse est cassée »
- Performances passées ≠ performances futures ; aucun rendement n'est garanti
