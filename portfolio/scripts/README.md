# Suivi quotidien par email — déploiement VPS

Rapport quotidien du plan d'investissement envoyé à `lucianobrulu@gmail.com` chaque matin à **7h34 heure Martinique**, avec gestion automatique des dates spéciales (résultats T2 le 4/08, lock-up le 6/08, **jour de démarrage les 7-8/08**, rappel DCA chaque 5 du mois).

## Installation (3 minutes, sur le VPS srv1518779 — même pattern que les agents LXD)

```bash
# 1. Récupérer le dossier portfolio sur le VPS
cd /root && git clone -b claude/financial-stock-skills-github-x4fpeo \
  https://github.com/Lucianobuju/ui-ux-pro-max-skill.git portfolio-repo

# 2. Dépendances
pip3 install yfinance requests

# 3. Configuration (réutiliser la clé Brevo LuxDog déjà en place)
echo 'export BREVO_API_KEY="xxx"' >> /root/.env          # clé existante Brevo
echo 'export SUIVI_EMAIL_FROM="contact@luxdog.store"' >> /root/.env  # expéditeur validé Brevo

# 4. Test immédiat
cd /root/portfolio-repo/portfolio/scripts && source /root/.env && python3 suivi_quotidien_email.py

# 5. Cron quotidien (11h34 UTC = 7h34 Martinique)
crontab -l | { cat; echo '34 11 * * * . /root/.env && cd /root/portfolio-repo/portfolio/scripts && python3 suivi_quotidien_email.py >> /root/suivi_email_cron.log 2>&1'; } | crontab -
```

Sans Brevo : configurer `SMTP_HOST`, `SMTP_PORT`, `SMTP_USER`, `SMTP_PASS` à la place (voie SMTP classique, ex. Gmail avec mot de passe d'application).

## Contenu du rapport

- Cours du jour : SPCX (USD), WPEA, PUST, EUR/USD (via Yahoo Finance) + variation vs veille
- SPCX vs prix d'IPO
- Alertes calendrier automatiques (4/08, 6/08, 7-8/08, chaque 5 du mois)
- Rappel des règles du plan verrouillé v1.0

## Complémentarité avec les agents Claude

| Canal | Fréquence | Rôle |
|---|---|---|
| **Email VPS** (ce script) | Quotidien | Rappel + cours bruts, fiable et indépendant |
| **Agents Claude** (`suivi-portefeuille` + `conseiller-portefeuille`) | Session/routine | Analyse complète, recommandations 🟢🟡🔴, mise à jour du JSON versionné |
| **Routine claude.ai** (à activer : nécessite une approbation) | Quotidien | Version native avec analyse + notification email intégrée |
