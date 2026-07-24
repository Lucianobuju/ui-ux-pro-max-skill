---
name: analyse-financiere
description: Boîte à outils d'analyse financière FR/US — ratios clés avec seuils d'interprétation, méthode DCF/WACC pas à pas, lecture des états financiers, différences IFRS vs US GAAP. À charger pour toute analyse de comptes, valorisation d'entreprise ou diagnostic financier.
---

# Analyse financière — méthode et outils

## Démarche de diagnostic en 5 étapes

1. **Activité et modèle économique** : que vend l'entreprise, à qui, avec quelles marges structurelles ? Positionner dans son secteur (comparer aux ratios sectoriels, pas dans l'absolu).
2. **Croissance et rentabilité** : CA, marge brute, EBITDA/EBE, résultat opérationnel, résultat net sur 3-5 ans. Chercher les tendances et les ruptures.
3. **Structure financière** : endettement, liquidité, solvabilité (voir `references/ratios.md`).
4. **Cash** : le résultat est une opinion, le cash est un fait. Analyser CAF, flux opérationnels, CAPEX, free cash-flow, variation du BFR.
5. **Valorisation** : croiser au moins 2 méthodes (DCF + multiples) et présenter une fourchette, jamais un point.

## DCF express

```
FCF = EBIT × (1 - taux d'IS) + D&A - CAPEX - ΔBFR
WACC = (E/V) × Ke + (D/V) × Kd × (1 - taux d'IS)
Ke (CAPM) = taux sans risque + β × prime de risque marché
Valeur terminale (Gordon) = FCF(n+1) / (WACC - g),  g < croissance PIB long terme
VE = Σ FCF actualisés + VT actualisée ;  Valeur des capitaux propres = VE - dette nette
```

Pièges : g ≥ WACC (absurde), oublier les minoritaires et provisions dans le bridge VE→equity, β non désendetté/réendetté pour les comparables.

## Réflexes FR vs US

- Comptes français : PCG, liasse fiscale (2050-2059), SIG (soldes intermédiaires de gestion) ; groupes cotés européens : IFRS
- Comptes US : US GAAP, 10-K (annuel), 10-Q (trimestriel), proxy statement (rémunérations) ; réconcilier les mesures non-GAAP (adjusted EBITDA) avec le GAAP — la différence est souvent instructive
- Différences clés IFRS/US GAAP : voir `references/ifrs-vs-usgaap.md`
- Vocabulaire : toujours donner les paires FR/EN (BFR/working capital, CAF/cash flow from operations approximé, EBE/EBITDA proche mais non identique)

## Sources primaires à privilégier

- France : comptes déposés (Pappers, BODACC), documents d'enregistrement universel (AMF/site émetteur), Banque de France (taux, séries)
- US : SEC EDGAR (10-K/10-Q/8-K), Fed (FRED pour les séries macro)
- Toujours dater les chiffres et vérifier en ligne les données de marché (taux sans risque, primes de risque, multiples sectoriels)
