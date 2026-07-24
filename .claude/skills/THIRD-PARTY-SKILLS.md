# Skills tiers vendorisés — attribution et licences

Les skills listés ci-dessous sont copiés depuis des dépôts open source sous licence MIT, conformément à leurs licences. Le texte des licences est reproduit intégralement en bas de ce fichier, comme l'exige la licence MIT.

## Sources

### [tradermonty/claude-trading-skills](https://github.com/tradermonty/claude-trading-skills) — MIT, commit `54fad29033fdd1982f555d53ec35d2031966a334`

- `technical-analyst` — analyse technique de graphiques hebdomadaires (tendances, supports/résistances, scénarios probabilisés)
- `us-stock-analysis` — analyse complète d'actions US (fondamental, technique, comparaisons, rapports)
- `market-environment-analysis` — analyse de l'environnement de marché global (risk-on/risk-off, secteurs, forex, matières premières)
- `options-strategy-advisor` — stratégies d'options (Black-Scholes, Greeks, simulation P/L, iron condors, earnings plays)
- `macro-regime-detector` — détection des transitions de régime macro (courbe des taux, crédit, concentration, rotations)

### [agiprolabs/claude-trading-skills](https://github.com/agiprolabs/claude-trading-skills) — MIT, commit `938a6ee84eed8f2b51cfb5055eaaddc8c596028d`

- `risk-management` — contrôles de risque au niveau portefeuille (drawdown, limites d'exposition, circuit breakers)
- `kelly-criterion` — dimensionnement optimal des positions (Kelly fractionnaire, estimation de l'edge)
- `portfolio-analytics` — mesure de performance (rendements, risque, ratios ajustés du risque, analyses glissantes)
- `tax-loss-harvesting` — identification et scoring des opportunités de récolte de moins-values, conformité wash sale
- `wash-sale-detection` — détection des wash sales (fenêtre 61 jours, suivi des pertes refusées)
- `cost-basis-engine` — calcul du prix de revient multi-méthodes (FIFO, LIFO, HIFO, identification spécifique)

### [romainsimon/paperasse](https://github.com/romainsimon/paperasse) — MIT, commit `c2a2ce3cba53d865ae26003eaaaff4a5ae7eec6c`

- `fiscaliste` — fiscalité personnelle française (IR, 2042, PFU, PEA, assurance-vie, LMNP, RSU/BSPCE, crypto, IFI, PER)
- `controleur-fiscal` — simulation de contrôle fiscal DGFIP (FEC, liasse, TVA, IS, chefs de redressement)
- `comptable` — comptabilité française (PCG, TVA, liasse 2033/2065, clôture, facturation électronique 2026)
- `commissaire-aux-comptes` — audit des comptes annuels (démarche NEP en 7 phases, opinion motivée)
- `notaire` — droit immobilier, successions, donations, démembrement, SCI, frais de notaire, projets d'actes

Modifications locales : suppression des dossiers `evals/` et des fichiers `*.example.json` ; le contenu des skills est inchangé.

### Non vendorisé volontairement

[openaccountants/openaccountants](https://github.com/openaccountants/openaccountants) (guides fiscaux 190+ juridictions relus par des CPA) est sous licence **AGPL-3.0**, incompatible avec une vendorisation dans ce dépôt MIT. Utilisable en complément via leur serveur MCP hébergé : `https://www.openaccountants.com/api/mcp`.

---

## Licence MIT — tradermonty/claude-trading-skills

```
MIT License

Copyright (c) 2026 TraderMonty

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## Licence MIT — agiprolabs/claude-trading-skills

```
MIT License

Copyright (c) 2026 AGIPro

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## Licence MIT — romainsimon/paperasse

```
MIT License

Copyright (c) 2026 Romain Simon

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
