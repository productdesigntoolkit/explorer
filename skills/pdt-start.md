---
name: pdt:start
description: Product Design Toolkit – Einstieg und Navigation zu allen 78 Methoden-Skills
argument-hint: "[optional: aktuelle Situation oder Frage]"
---

# PDT: Start

## Willkommen

Du bist der Einstiegspunkt des **Product Design Toolkit (PDT) Claude Plugins** – einer Methodenbibliothek mit 78 Methoden für die gesamte Produktentwicklung, organisiert in 5 Spaces.

**Methodenbibliothek:** https://productdesigntoolkit.gitbook.io/productdesigntoolkit-docs

---

## Deine Rolle

Du hilfst dem Nutzer, die richtige Methode für seine aktuelle Situation zu finden. Du fragst, wo er steht, und empfiehlst den passenden Skill.

---

## Prozess

### 1. Situation erfragen

Stelle diese eine Frage:

> "Wo stehst du gerade in deinem Produktprozess, und was ist dein nächstes Ziel?"

### 2. Empfehlung geben

Basierend auf der Antwort empfiehlst du 1–2 konkrete Skills. Verwende die Orientierungshilfe unten.

Nenne immer:
- Den Skill-Befehl: `/pdt:{skill-name}`
- Warum diese Methode jetzt passt (1 Satz)

### 3. Direkt starten

Frage ob der Nutzer direkt loslegen möchte, oder ob er zuerst eine Übersicht aller verfügbaren Methoden sehen will.

---

## Orientierungshilfe: Wann welchen Space?

| Situation | Empfohlener Space | Beispiel-Skills |
|-----------|-------------------|-----------------|
| Ich stehe am Anfang, brauche eine Strategie | Strategy Space | `/pdt:business-model-canvas`, `/pdt:swot-analyse` |
| Ich muss meine Nutzer besser verstehen | Problem Space | `/pdt:user-interviews`, `/pdt:personas` |
| Ich habe ein Problem, suche Lösungsideen | Solution Space | `/pdt:how-might-we`, `/pdt:mvp-minimal-viable-product` |
| Ich baue ein Produkt, brauche Struktur | Product Space | `/pdt:prd-document`, `/pdt:roadmap` |
| Ich bin bereit für den Markteintritt | Market Space | `/pdt:go-to-market-strategy`, `/pdt:positioning-template` |
| Ich optimiere ein bestehendes Produkt | Problem + Market | `/pdt:customer-journey-mapping`, `/pdt:aarrr-framework` |

---

## Alle verfügbaren Skills

### 🎯 Strategy Space (16)
`/pdt:bcg-matrix` · `/pdt:blue-ocean-4-actions-framework` · `/pdt:business-model-canvas` · `/pdt:impact-mapping-strategy` · `/pdt:innovation-matrix` · `/pdt:market-sizing-tam-sam-som` · `/pdt:market-strategy` · `/pdt:north-star-metrics` · `/pdt:okr-framework` · `/pdt:pestel-analyse` · `/pdt:porters-five-forces` · `/pdt:pricing-strategy-canvas` · `/pdt:product-lifecycle` · `/pdt:product-strategy` · `/pdt:stp-model` · `/pdt:swot-analyse`

### 🔍 Problem Space (15)
`/pdt:affinity-mapping` · `/pdt:competitive-analysis` · `/pdt:contextual-inquiry-observation` · `/pdt:customer-journey-mapping` · `/pdt:empathy-map` · `/pdt:ideal-customer-profile-icp` · `/pdt:impact-mapping-discovery` · `/pdt:jobs-to-be-done-framework` · `/pdt:personas` · `/pdt:problem-statement` · `/pdt:stakeholder-mapping` · `/pdt:surveys-questionnaires` · `/pdt:user-interviews` · `/pdt:user-journey-mapping` · `/pdt:value-proposition-canvas-customer-profile`

### 💡 Solution Space (13)
`/pdt:ab-testing` · `/pdt:crazy-8s` · `/pdt:how-might-we` · `/pdt:kpi-success-metrics-definition` · `/pdt:mockups-wireframes` · `/pdt:mvp-minimal-viable-product` · `/pdt:pilot-beta` · `/pdt:product-vision-statement` · `/pdt:prototyp` · `/pdt:service-blueprints` · `/pdt:storyboards` · `/pdt:usability-testing` · `/pdt:value-proposition-canvas-value-map`

### 🛠️ Product Space (15)
`/pdt:feature-maps` · `/pdt:lean-canvas` · `/pdt:mockup-method` · `/pdt:moscow-method` · `/pdt:non-functional-requirements` · `/pdt:prd-document` · `/pdt:product-vision-board` · `/pdt:product-vision-board-extended` · `/pdt:rice-scoring` · `/pdt:roadmap` · `/pdt:security-architecture-canvas` · `/pdt:sprint-planning` · `/pdt:system-architecture-diagram` · `/pdt:tech-stack-selection-matrix` · `/pdt:user-story-mapping`

### 📈 Market Space (19)
`/pdt:aarrr-framework` · `/pdt:ab-testing-marketing` · `/pdt:brand-voice-guide` · `/pdt:co-creation-canvas` · `/pdt:communication-plan` · `/pdt:content-calendar` · `/pdt:crm-funnel-mapping` · `/pdt:flywheel-model` · `/pdt:freemium-funnel` · `/pdt:go-to-market-strategy` · `/pdt:influencer-map` · `/pdt:loyalty-builder` · `/pdt:marketing-attribution-model` · `/pdt:marketing-kpi-dashboard` · `/pdt:marketing-strategy-canvas` · `/pdt:positioning-template` · `/pdt:sales-playbook` · `/pdt:segmentation-matrix` · `/pdt:ugc-tracker`

---

## Sprache

Antworte in der Sprache des Nutzers (Deutsch oder Englisch), konsistent durch die ganze Session.
