---
title: "System Architecture Diagram"
space: product-space
description: "Ein System Architecture Diagram visualisiert die technische Struktur eines digitalen Produkts und zeigt die Beziehungen zwischen verschiedenen Komponenten, Services und Datenflüssen auf."
skill: system-architecture-diagram
---

# System Architecture Diagram

## Kurzbeschreibung
Ein System Architecture Diagram visualisiert die technische Struktur eines digitalen Produkts und zeigt die Beziehungen zwischen verschiedenen Komponenten, Services und Datenflüssen auf. Diese Methode hilft dabei, komplexe Systemlandschaften verständlich zu machen und technische Entscheidungen zu dokumentieren.

## Einsatzzweck
Das System Architecture Diagram wird in der Entwicklungsphase eingesetzt, um die technische Architektur zu planen, zu kommunizieren und zu dokumentieren. Es eignet sich besonders bei komplexen digitalen Produkten mit mehreren integrierten Services, APIs oder Datenbanken.

## Kurzanleitung
1. **System-Scope definieren:** Bestimme die Grenzen deines Systems und welche Komponenten einbezogen werden → Web-App, Mobile-App, Backend-Services
2. **Hauptkomponenten identifizieren:** Liste alle wichtigen Systemteile auf → Frontend, Backend, Datenbank, externe APIs, Mikroservices
3. **Architektur-Layer festlegen:** Strukturiere das System in logische Ebenen → Präsentationsschicht, Business-Logic, Datenschicht
4. **Datenflüsse mapping:** Zeichne die Verbindungen und Datenströme zwischen den Komponenten → HTTP-Requests, Database-Queries, API-Calls
5. **Technologie-Stack ergänzen:** Füge verwendete Technologien und Frameworks hinzu → React, Node.js, PostgreSQL, AWS
6. **Externe Abhängigkeiten markieren:** Kennzeichne Third-Party-Services und externe Schnittstellen → Payment-Provider, Authentication-Service
7. **Sicherheitsaspekte einzeichnen:** Zeige Authentifizierung, Autorisierung und sichere Verbindungen → HTTPS, JWT-Token, Firewalls
8. **Skalierungskonzepte visualisieren:** Dokumentiere Load Balancer, Caching und Redundanzen → CDN, Redis-Cache, Multiple Server-Instanzen

## Beispielprompt
{% code overflow="wrap" %}
```
Erstelle ein System Architecture Diagram für eine E-Commerce-Plattform mit folgenden Anforderungen: React-Frontend, Node.js-Backend, PostgreSQL-Datenbank, Stripe-Payment, AWS-Hosting. Zeige auch Caching-Layer und externe APIs für Produktkatalog.
```
{% endcode %}

## Quellen

**Autor:** Industrie-Praxis (Software Engineering, C4-Modell u.a.)
**Werk:** Etablierte Praxis aus Software Architecture und System Design
**Link:** [C4 Model](https://c4model.com/)
**Typ:** industrie-praxis

**Ergänzende Quellen:**

* Website: [C4 Model — Simon Brown](https://c4model.com/)
* Buch: Len Bass, Paul Clements, Rick Kazman — _Software Architecture in Practice_, Addison-Wesley (2012)
* Website: [AWS Architecture Center](https://aws.amazon.com/architecture/)
