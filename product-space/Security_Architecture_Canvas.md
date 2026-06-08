---
title: "Security Architecture Canvas"
space: product-space
description: "Das Security Architecture Canvas ist ein strukturiertes Framework zur systematischen Planung und Visualisierung der Sicherheitsarchitektur eines digitalen Products."
---

# Security Architecture Canvas

## Kurzbeschreibung
Das Security Architecture Canvas ist ein strukturiertes Framework zur systematischen Planung und Visualisierung der Sicherheitsarchitektur eines digitalen Products. Es hilft Teams dabei, alle sicherheitsrelevanten Aspekte von der Identitätsverwaltung bis zur Compliance in einem übersichtlichen Canvas zu erfassen und zu koordinieren.

## Einsatzzweck
Diese Methode wird eingesetzt, wenn die Sicherheitsarchitektur eines digitalen Products oder Systems geplant, dokumentiert oder überprüft werden soll. Besonders wertvoll ist sie in frühen Entwicklungsphasen, bei Sicherheitsaudits oder wenn verschiedene Stakeholder ein gemeinsames Verständnis der Sicherheitsanforderungen entwickeln müssen.

## Kurzanleitung
1. **Canvas vorbereiten:** Erstelle das Security Architecture Canvas mit den neun Hauptbereichen: Assets, Threats, Identity & Access, Data Protection, Infrastructure Security, Application Security, Monitoring & Response, Compliance und Business Continuity
2. **Assets identifizieren:** Liste alle schützenswerten Ressourcen auf → Kundendaten, geistiges Eigentum, Systemkomponenten, Reputation
3. **Bedrohungen analysieren:** Erfasse potenzielle Sicherheitsrisiken und Angriffsvektoren → Cyberattacken, Datenlecks, Social Engineering, Systemausfälle
4. **Zugriffskontrolle definieren:** Plane Authentifizierung, Autorisierung und Benutzerverwaltung → Multi-Faktor-Authentifizierung, Rollenverwaltung, Single Sign-On
5. **Datenschutz konzipieren:** Definiere Verschlüsselung, Datenklassifizierung und Schutzmassnnahmen → Ende-zu-Ende-Verschlüsselung, Anonymisierung, sichere Speicherung
6. **Infrastruktursicherheit planen:** Erfasse Netzwerksicherheit, Server-Härtung und Cloud-Security → Firewalls, VPN, sichere Container-Konfiguration
7. **Anwendungssicherheit sicherstellen:** Plane Code-Sicherheit, API-Schutz und sichere Entwicklung → Input-Validierung, OWASP-Guidelines, Security Testing
8. **Überwachung etablieren:** Definiere Monitoring, Incident Response und Logging → SIEM-Systeme, Alerting, Forensik-Capabilities
9. **Compliance validieren:** Erfasse gesetzliche Anforderungen und Zertifizierungen → DSGVO, ISO 27001, branchenspezifische Standards

## Beispielprompt
{% code overflow="wrap" %}
```
Erstelle ein Security Architecture Canvas für eine E-Commerce-Plattform mit 100.000 Nutzern. Berücksichtige dabei Zahlungsverarbeitung, Kundendatenmanagement und internationale Compliance-Anforderungen. Fokussiere auf die kritischsten Sicherheitsaspekte.
```
{% endcode %}

## Quellen

**Autor:** Industrie-Praxis (OWASP, NIST, Security-Community)
**Werk:** Etablierte Praxis aus IT-Security, Threat Modeling und Secure-by-Design
**Link:** [OWASP — Top Ten](https://owasp.org/www-project-top-ten/)
**Typ:** industrie-praxis

**Ergänzende Quellen:**

* Website: [OWASP — Top Ten](https://owasp.org/www-project-top-ten/)
* Website: [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)
* Buch: Adam Shostack — _Threat Modeling: Designing for Security_, Wiley (2014)
