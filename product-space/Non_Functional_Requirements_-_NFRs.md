---
title: "Non Functional Requirements - NFRs"
space: product-space
description: "Non Functional Requirements (NFRs) definieren die Qualitätsanforderungen eines Systems wie Performance, Sicherheit und Benutzerfreundlichkeit."
---

# Non Functional Requirements - NFRs

## Kurzbeschreibung

Non Functional Requirements (NFRs) definieren die Qualitätsanforderungen eines Systems wie Performance, Sicherheit und Benutzerfreundlichkeit. Sie ergänzen die funktionalen Anforderungen und stellen sicher, dass das Produkt nicht nur die richtigen Funktionen hat, sondern diese auch in der gewünschten Qualität bereitstellt.

## Einsatzzweck

NFRs werden in der Anforderungsanalyse und Systemarchitektur eingesetzt, um messbare Qualitätskriterien zu definieren. Sie sind besonders wichtig bei komplexen Systemen, kritischen Anwendungen und wenn spezifische Performance- oder Sicherheitsstandards erfüllt werden müssen.

## Kurzanleitung

1. **Kategorien identifizieren:** Bestimme relevante NFR-Kategorien wie Performance, Sicherheit, Usability, Verfügbarkeit, Skalierbarkeit
2. **Stakeholder einbeziehen:** Sammle Qualitätsanforderungen von allen relevanten Interessensgruppen: Endnutzer, IT-Betrieb, Compliance
3. **Messbare Kriterien definieren:** Formuliere spezifische, quantifizierbare Anforderungen → "Antwortzeit unter 2 Sekunden" statt "schnell"
4. **Prioritäten setzen:** Bewerte NFRs nach Wichtigkeit und Auswirkung auf das Geschäftsziel
5. **Akzeptanzkriterien festlegen:** Definiere klare Testkriterien für jede Anforderung
6. **Abhängigkeiten analysieren:** Identifiziere Konflikte zwischen verschiedenen NFRs → Sicherheit vs. Performance
7. **Architektur-Impact bewerten:** Prüfe, wie NFRs die Systemarchitektur beeinflussen
8. **Dokumentation erstellen:** Erfasse alle NFRs strukturiert mit Begründung und Messkriterien

## Beispielprompt

{% code overflow="wrap" %}
```
# Requirements Quick List Prompt

## Rolle
Du bist Business Analyst und schreibst pragmatische Anforderungslisten ohne Bürokratie-Overhead.

## Kontext
**Projekt:** [Name]
**Kurzbeschreibung:** [2 bis 3 Sätze, was gebaut werden soll]
**Zielgruppe:** [Wer nutzt es?]

## Aufgabe
Erstelle eine einfache, übersichtliche Tabelle mit Functional und Non-Functional Requirements. Keine Schnörkel, keine Romane; jede Zeile eine Anforderung.

## Output-Format

### Functional Requirements

| ID | Idee | Akzeptanzkriterium | Quelle | Status | Priorität | Gruppe |
|----|------|--------------------|--------|--------|-----------|--------|
| FR-001 | Nutzer kann sich per E-Mail registrieren | Given gültige E-Mail, when Registrierung abgeschickt, then Bestätigungsmail in unter 30s | Product Owner | Draft | Must | Authentication |
| FR-002 | Nutzer kann Passwort zurücksetzen | Reset-Link gültig 60 Min, neues Passwort erfüllt Policy | Security Lead | Draft | Must | Authentication |
| FR-003 | Nutzer sieht Dashboard mit aktuellen KPIs | K
```
{% endcode %}

## Quellen

**Autor:** IEEE / ISO 25010 (Software-Engineering-Standard) **Werk:** ISO/IEC 25010:2011 _Systems and software Quality Requirements and Evaluation (SQuaRE)_ **Jahr:** 2011 (ISO) **Link:** [ISO 25010](https://iso25000.com/index.php/en/iso-25000-standards/iso-25010) **Typ:** kanonisch

**Ergänzende Quellen:**

* Standard: ISO/IEC 25010:2011 — _Systems and software Quality Requirements and Evaluation (SQuaRE)_
* Buch: Ian Sommerville — _Software Engineering_, Pearson (2016)
* Website: [ISO 25010 — Quality Model](https://iso25000.com/index.php/en/iso-25000-standards/iso-25010)
