---
name: fiscalite-investisseur
description: Boîte à outils fiscale FR/US pour l'investisseur — méthode de simulation PFU vs barème, règles PEA/assurance-vie/PER/crypto, barèmes et abattements de référence, fiscalité US des gains (capital gains, wash sales, formulaires), checklists déclaratives (2042 et annexes, 8949/Schedule D). À charger pour tout calcul d'impôt, comparaison d'enveloppes ou préparation de déclaration.
---

# Fiscalité de l'investisseur — méthode et outils

## Méthode de toute simulation fiscale

1. **Résidence fiscale et année** : critères de l'article 4 B CGI côté FR, substantial presence test côté US ; en cas de conflit, critères conventionnels successifs (foyer permanent → centre des intérêts vitaux → séjour habituel → nationalité)
2. **Qualifier le revenu** : catégorie (RCM, plus-value mobilière, foncier, BIC/BNC, salaire) — la qualification détermine le régime
3. **Vérifier les chiffres de l'année en ligne** : barèmes, plafonds et abattements changent à chaque loi de finances — les valeurs dans `references/bareme-fr.md` et `references/fiscalite-us.md` sont des références à confirmer
4. **Simuler toutes les options** : PFU vs barème (option globale, pas ligne à ligne), micro vs réel, etc. — avec hypothèses explicites et montants chiffrés
5. **Checklist déclarative** : formulaires, cases, échéances

## Décisions rapides (résident fiscal français)

- **PFU (30 %) vs barème** : le barème gagne généralement si TMI ≤ 11 % (dividendes avec abattement 40 % : parfois même à 30 % — simuler) ; l'option barème est globale pour tous les RCM et PV de l'année et ouvre la CSG déductible (6,8 %)
- **PEA vs CTO** : PEA prioritaire pour tout ce qui y est éligible dès que l'horizon dépasse 5 ans (gains exonérés d'IR, seuls les 17,2 % de PS restent)
- **Assurance-vie** : prendre date tôt ; rachats après 8 ans avec abattement 4 600/9 200 € de gains par an = quasi-exonération d'IR en gestion habile
- **Crypto (particulier)** : article 150 VH bis — imposition uniquement lors de la conversion en monnaie fiat ou achat de biens/services (les échanges crypto-crypto sont neutres) ; flat tax 30 % ou option barème (12,8 % → barème depuis 2023) ; cession annuelle < 305 € exonérée ; activité habituelle assimilable à du BNC
- **Moins-values mobilières** : imputables sur les plus-values de même nature de l'année puis reportables 10 ans — penser à les matérialiser avant le 31 décembre si des gains sont réalisés (tax-loss harvesting à la française, sans règle de wash sale en droit FR — mais l'abus de droit reste possible sur les allers-retours purement fiscaux)

## Décisions rapides (contribuable US)

- Détenir >1 an avant de vendre quand c'est possible : long-term capital gains (0/15/20 %) vs short-term (barème ordinaire jusqu'à 37 %)
- **Wash sale rule** : rachat d'un titre « substantially identical » dans les 30 jours avant/après une vente à perte → perte non déductible (report sur le prix de revient) ; ne s'applique pas aux gains
- **Tax-loss harvesting** : vendre les positions perdantes pour compenser les gains ; jusqu'à 3 000 $/an de pertes nettes imputables sur le revenu ordinaire, report illimité au-delà
- Ordre de remplissage des enveloppes : 401(k) jusqu'au match → HSA → Roth/Traditional IRA → 401(k) au plafond → brokerage

## Transfrontalier FR-US : voir `references/fiscalite-us.md` (convention, FATCA, PFIC, formulaires)

## Ligne rouge

Optimiser = utiliser les dispositifs prévus par la loi. Refuser toute dissimulation, minoration ou montage sans substance (abus de droit L64 LPF côté FR, economic substance doctrine côté US). En cas de doute sur un montage : le décrire honnêtement, signaler le risque de requalification, recommander un professionnel.
