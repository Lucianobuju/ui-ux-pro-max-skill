# Équipe d'agents experts — Finance, Bourse, Droit, Fiscalité

Quatre agents spécialisés utilisables dans Claude Code via le Task tool (ils sont détectés automatiquement depuis `.claude/agents/`).

| Agent | Domaine | Quand l'utiliser |
|---|---|---|
| `expert-finance` | Finance générale FR/US | Analyse financière, comptabilité (PCG, IFRS, US GAAP), banque, macro, produits d'épargne, corporate finance |
| `expert-bourse` | Bourse & investissements | Analyse d'actions/ETF/options, valorisation, allocation de portefeuille, stratégies, enveloppes (PEA, CTO, 401k) |
| `expert-droit-affaires` | Droit des affaires FR/EU/US | Formes sociales, contrats, pactes, levées de fonds, réglementation AMF/SEC, RGPD |
| `expert-fiscalite` | Fiscalité FR/US | IR, PFU, PEA, assurance-vie, crypto, IS/TVA, IFI, IRS (capital gains, wash sales), situations franco-américaines |

## Routage entre agents

Chaque agent connaît ses limites et renvoie vers le spécialiste compétent :

- Question de **sélection de titres** posée à `expert-finance` → `expert-bourse`
- Question d'**impôt sur les gains** posée à `expert-bourse` → `expert-fiscalite`
- Question de **structure juridique** posée à `expert-fiscalite` → `expert-droit-affaires`
- Question de **modélisation financière** posée à `expert-droit-affaires` → `expert-finance`

Pour une question transverse (ex. « je vends ma société : prix, structuration, impôt ? »), lancer plusieurs agents en parallèle et synthétiser leurs réponses.

## Exemple d'invocation

Dans une conversation Claude Code :

> Utilise l'agent expert-fiscalite pour comparer PFU et barème progressif sur 10 000 € de dividendes avec un TMI à 30 %.

Ou en parallèle :

> Lance expert-bourse pour analyser la valorisation de LVMH et expert-fiscalite pour la fiscalité d'un achat en PEA vs CTO.

## Avertissement

Ces agents produisent de l'information et de l'analyse à visée pédagogique. Ils ne remplacent ni un conseiller en investissements financiers (CIF), ni un avocat, ni un expert-comptable ou avocat fiscaliste. Vérifier les chiffres et textes cités : barèmes et lois changent chaque année.
