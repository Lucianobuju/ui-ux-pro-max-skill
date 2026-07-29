# Équipe d'agents experts — Finance, Bourse, Droit, Fiscalité

Quatre agents spécialisés utilisables dans Claude Code via le Task tool (ils sont détectés automatiquement depuis `.claude/agents/`).

| Agent | Domaine | Quand l'utiliser |
|---|---|---|
| `expert-finance` | Finance générale FR/US | Analyse financière, comptabilité (PCG, IFRS, US GAAP), banque, macro, produits d'épargne, corporate finance |
| `expert-bourse` | Bourse & investissements | Analyse d'actions/ETF/options, valorisation, allocation de portefeuille, stratégies, enveloppes (PEA, CTO, 401k) |
| `expert-droit-affaires` | Droit des affaires FR/EU/US | Formes sociales, contrats, pactes, levées de fonds, réglementation AMF/SEC, RGPD |
| `expert-fiscalite` | Fiscalité FR/US | IR, PFU, PEA, assurance-vie, crypto, IS/TVA, IFI, IRS (capital gains, wash sales), situations franco-américaines |

## Skills de domaine

Chaque agent charge obligatoirement son skill de domaine (`.claude/skills/`) avant de répondre — méthodes, formules, barèmes et checklists :

| Agent | Skill | Références incluses |
|---|---|---|
| `expert-finance` | `analyse-financiere` | Ratios avec seuils d'interprétation, DCF/WACC, IFRS vs US GAAP |
| `expert-bourse` | `analyse-boursiere` | Multiples de valorisation par secteur, comparatif des enveloppes FR/US |
| `expert-droit-affaires` | `droit-des-affaires` | Comparatif des formes sociales FR/US, checklist de clauses contractuelles |
| `expert-fiscalite` | `fiscalite-investisseur` | Barèmes FR (IR, PFU, IFI, transmission), fiscalité US et transfrontalière |

Les barèmes et seuils datent de la rédaction : les agents ont pour consigne de vérifier en ligne les valeurs de l'année concernée avant de chiffrer.

## Skills avancés (vendorisés depuis GitHub, licence MIT)

En plus de son skill de base, chaque agent dispose de skills spécialisés issus des meilleurs dépôts open source (voir `.claude/skills/THIRD-PARTY-SKILLS.md` pour l'attribution complète) :

| Agent | Skills avancés |
|---|---|
| `expert-finance` | `macro-regime-detector`, `comptable`, `commissaire-aux-comptes` |
| `expert-bourse` | `us-stock-analysis`, `technical-analyst`, `market-environment-analysis`, `options-strategy-advisor`, `risk-management`, `kelly-criterion`, `portfolio-analytics` |
| `expert-droit-affaires` | `notaire` |
| `expert-fiscalite` | `fiscaliste`, `controleur-fiscal`, `comptable`, `tax-loss-harvesting`, `wash-sale-detection`, `cost-basis-engine` |

Sources : [tradermonty/claude-trading-skills](https://github.com/tradermonty/claude-trading-skills), [agiprolabs/claude-trading-skills](https://github.com/agiprolabs/claude-trading-skills), [romainsimon/paperasse](https://github.com/romainsimon/paperasse) — tous MIT. Les agents chargent ces skills à la demande selon la mission, pas systématiquement.

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
