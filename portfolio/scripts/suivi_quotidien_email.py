#!/usr/bin/env python3
"""Suivi quotidien du plan d'investissement 5 ans — envoi par email.

Conçu pour tourner en cron sur le VPS (même pattern que les agents LXD) :
    34 11 * * * cd /root/portfolio && python3 suivi_quotidien_email.py
    (11h34 UTC = 7h34 Martinique)

Dépendances : pip3 install yfinance requests
Configuration par variables d'environnement (dans ~/.env ou le crontab) :
    BREVO_API_KEY=...           # voie 1 (recommandée: Brevo déjà utilisé pour LuxDog)
    # ou SMTP_HOST / SMTP_PORT / SMTP_USER / SMTP_PASS   # voie 2
    SUIVI_EMAIL_TO=lucianobrulu@gmail.com
    SUIVI_EMAIL_FROM=...        # expéditeur validé Brevo/SMTP
"""
import json
import os
import sys
from datetime import date, datetime, timezone
from pathlib import Path

PLAN_PATH = Path(__file__).resolve().parent.parent / "portefeuille.json"
TICKERS = {"SPCX": "SPCX", "WORLD": "WPEA.PA", "NDX": "PUST.PA", "EURUSD": "EURUSD=X"}
EMAIL_TO = os.environ.get("SUIVI_EMAIL_TO", "lucianobrulu@gmail.com")
EMAIL_FROM = os.environ.get("SUIVI_EMAIL_FROM", EMAIL_TO)


def get_prices():
    import yfinance as yf
    out = {}
    for name, ticker in TICKERS.items():
        try:
            h = yf.Ticker(ticker).history(period="5d")["Close"].dropna()
            out[name] = {
                "dernier": round(float(h.iloc[-1]), 2),
                "veille_pct": round((h.iloc[-1] / h.iloc[-2] - 1) * 100, 2) if len(h) > 1 else None,
            }
        except Exception as e:  # marché fermé, ticker indispo: on le dit, on n'invente pas
            out[name] = {"erreur": str(e)[:80]}
    return out


def build_report(plan, prices):
    today = date.today()
    lines = [f"SUIVI PORTEFEUILLE 5 ANS - {today.strftime('%d/%m/%Y')}", ""]

    # Événements spéciaux
    specials = {
        date(2026, 8, 4): ">>> AUJOURD'HUI : résultats T2 SpaceX — observer, ne pas acheter.",
        date(2026, 8, 5): ">>> Demain : expiration du lock-up SPCX (~911 M d'actions).",
        date(2026, 8, 6): ">>> AUJOURD'HUI : expiration du lock-up SPCX — observer les flux.",
        date(2026, 8, 7): ">>> JOUR DE DEMARRAGE ! Ordres à passer : 195 EUR WPEA + 75 EUR PUST (PEA) + 30 EUR SPCX (eToro, x1, eToro Money).",
        date(2026, 8, 8): ">>> JOUR DE DEMARRAGE (option 2) ! Mêmes ordres si non passés hier.",
    }
    if today in specials:
        lines += [specials[today], ""]
    if today.day == 5:
        lines += [">>> C'est le 5 : DCA du mois — 195 EUR WPEA + 75 EUR PUST + 30 EUR SPCX (300 EUR).", ""]

    lines.append("Cours du jour :")
    labels = {"SPCX": "SpaceX (USD)", "WORLD": "WPEA MSCI World (EUR)", "NDX": "PUST Nasdaq-100 (EUR)", "EURUSD": "EUR/USD"}
    for k, lbl in labels.items():
        p = prices.get(k, {})
        if "erreur" in p:
            lines.append(f"  - {lbl} : indisponible ({p['erreur']})")
        else:
            var = f" ({p['veille_pct']:+.2f} % vs veille)" if p.get("veille_pct") is not None else ""
            lines.append(f"  - {lbl} : {p['dernier']}{var}")

    # Repères du plan
    ref = plan.get("references_marche", {})
    spcx = prices.get("SPCX", {})
    if "dernier" in spcx and ref.get("spcx_prix_ipo_usd"):
        ipo = ref["spcx_prix_ipo_usd"]
        lines += ["", f"SPCX vs prix d'IPO ({ipo} $) : {(spcx['dernier'] / ipo - 1) * 100:+.1f} %"]

    # Positions (une fois le portefeuille démarré, alimentées par l'agent suivi-portefeuille)
    if not plan.get("positions"):
        lines += ["", "Portefeuille : pas encore démarré (démarrage prévu 7-8 août)."]

    lines += [
        "",
        "Rappel plan verrouillé v1.0 : 300 EUR/mois (195 WPEA / 75 PUST / 30 SPCX), DCA le 5,",
        "jamais de vente panique, SPCX plafonné à 12 %.",
        "",
        "Ceci est un rapport automatique d'information, pas un conseil en investissement.",
    ]
    return "\n".join(lines)


def send_email(subject, body):
    api_key = os.environ.get("BREVO_API_KEY")
    if api_key:
        import requests
        r = requests.post(
            "https://api.brevo.com/v3/smtp/email",
            headers={"api-key": api_key, "content-type": "application/json"},
            json={
                "sender": {"email": EMAIL_FROM, "name": "Suivi Portefeuille"},
                "to": [{"email": EMAIL_TO}],
                "subject": subject,
                "textContent": body,
            },
            timeout=30,
        )
        r.raise_for_status()
        return "brevo"
    host = os.environ.get("SMTP_HOST")
    if host:
        import smtplib
        from email.mime.text import MIMEText
        msg = MIMEText(body, "plain", "utf-8")
        msg["Subject"], msg["From"], msg["To"] = subject, EMAIL_FROM, EMAIL_TO
        with smtplib.SMTP_SSL(host, int(os.environ.get("SMTP_PORT", 465))) as s:
            s.login(os.environ["SMTP_USER"], os.environ["SMTP_PASS"])
            s.sendmail(EMAIL_FROM, [EMAIL_TO], msg.as_string())
        return "smtp"
    raise SystemExit("Configurer BREVO_API_KEY ou SMTP_HOST/SMTP_USER/SMTP_PASS")


def main():
    plan = json.loads(PLAN_PATH.read_text(encoding="utf-8"))
    prices = get_prices()
    body = build_report(plan, prices)
    subject = f"📈 Suivi portefeuille — {date.today().strftime('%d/%m/%Y')}"
    via = send_email(subject, body)
    # Trace locale pour l'historique (le JSON versionné reste géré par l'agent Claude)
    log = PLAN_PATH.parent / "suivi_email.log"
    with log.open("a", encoding="utf-8") as f:
        f.write(f"{datetime.now(timezone.utc).isoformat()} sent via {via}\n")
    print(f"Rapport envoyé à {EMAIL_TO} via {via}")


if __name__ == "__main__":
    main()
