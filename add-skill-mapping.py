#!/usr/bin/env python3
"""Add skill: field to method frontmatter based on explicit mapping."""

import os, re

ROOT = os.path.dirname(os.path.abspath(__file__))

SKILL_MAP = {
    # Strategy Space
    "BCG_Matrix":                          "bcg-matrix",
    "Blue_Ocean_4_Actions_Framework":      "blue-ocean-4-actions-framework",
    "Business_Model_Canvas":               "business-model-canvas",
    "Impact_Mapping_Strategy_":            "impact-mapping-strategy",
    "Innovationsmatrix":                   "innovation-matrix",
    "Market_Sizing_TAM_SAM_SOM_":          "market-sizing-tam-sam-som",
    "Marktstrategie":                      "market-strategy",
    "North_Star_Metrics":                  "north-star-metrics",
    "OKR_Framework":                       "okr-framework",
    "PESTEL_Analyse":                      "pestel-analyse",
    "Porters_Five_Forces":                 "porters-five-forces",
    "Pricing_Strategy_Canvas":             "pricing-strategy-canvas",
    "Product_Lifecycle":                   "product-lifecycle",
    "Produktstrategie":                    "product-strategy",
    "STP_Model":                           "stp-model",
    "SWOT_Analyse":                        "swot-analyse",
    # Problem Space
    "Affinity_Mapping":                    "affinity-mapping",
    "Competitive_Analysis":                "competitive-analysis",
    "Contextual_Inquiry_-_Observation":    "contextual-inquiry-observation",
    "Customer_Journey_Mapping":            "customer-journey-mapping",
    "Empathy_Maps":                        "empathy-map",
    "Ideal_Customer_Profile_ICP":          "ideal-customer-profile-icp",
    "Impact_Mapping_Discovery_":           "impact-mapping-discovery",
    "Jobs-to-be-Done_Framework":           "jobs-to-be-done-framework",
    "Personas":                            "personas",
    "Problem_Statement":                   "problem-statement",
    "Stakeholder_Mapping":                 "stakeholder-mapping",
    "Surveys_Questionnaires":              "surveys-questionnaires",
    "User_Interviews":                     "user-interviews",
    "User_Journey_Mapping":                "user-journey-mapping",
    "Value_Proposition_Canvas_Customer_Profile": "value-proposition-canvas-customer-profile",
    # Solution Space
    "A_B_Testing":                         "ab-testing",
    "Crazy_8s":                            "crazy-8s",
    "How_Might_We_Questions":              "how-might-we",
    "Key_Performance_Indicators_-_KPI":    "kpi-success-metrics-definition",
    "Mockups":                             "mockups-wireframes",
    "MVP_-_Minimal_Viable_Product":        "mvp-minimal-viable-product",
    "Pilot_Beta":                          "pilot-beta",
    "Product_Vision_Statement":            "product-vision-statement",
    "Prototype":                           "prototyp",
    "Service_Blueprints":                  "service-blueprints",
    "Storyboards":                         "storyboards",
    "Usability_Testing":                   "usability-testing",
    "Value_Proposition_Canvas_Value_Map":  "value-proposition-canvas-value-map",
    # Product Space
    "Feature_Maps":                        "feature-maps",
    "Lean_Canvas":                         "lean-canvas",
    "Mockup_Method":                       "mockup-method",
    "MoSCoW_Method":                       "moscow-method",
    "Non_Functional_Requirements_-_NFRs":  "non-functional-requirements",
    "PRD_Document":                        "prd-document",
    "Product_Vision_Board_Extended":       "product-vision-board-extended",
    "Product_Vision_Board":                "product-vision-board",
    "RICE_Scoring":                        "rice-scoring",
    "Roadmap":                             "roadmap",
    "Security_Architecture_Canvas":        "security-architecture-canvas",
    "Sprint_Planning":                     "sprint-planning",
    "System_Architecture_Diagram":         "system-architecture-diagram",
    "Tech_Stack_Selection_Matrix":         "tech-stack-selection-matrix",
    "User_Story_Mapping":                  "user-story-mapping",
    # Market Space
    "AARRR_Framework":                     "aarrr-framework",
    "A_B_Testing_Marketing":               "ab-testing-marketing",
    "Brand_Voice_Guide":                   "brand-voice-guide",
    "Co-Creation_Canvas":                  "co-creation-canvas",
    "Communication_Plan":                  "communication-plan",
    "Content_Calendar":                    "content-calendar",
    "CRM_Funnel_Mapping":                  "crm-funnel-mapping",
    "Customer_Segmentation_Matrix":        "segmentation-matrix",
    "Flywheel_Model":                      "flywheel-model",
    "Freemium_Funnel":                     "freemium-funnel",
    "Go_To_Market_Strategy":               "go-to-market-strategy",
    "Influencer_Map":                      "influencer-map",
    "Loyalty_Builder":                     "loyalty-builder",
    "Marketing_Attribution_Model":         "marketing-attribution-model",
    "Marketing_KPI_Dashboard":             "marketing-kpi-dashboard",
    "Marketing_Strategy_Canvas":           "marketing-strategy-canvas",
    "Positioning_Template":                "positioning-template",
    "Sales_Playbook":                      "sales-playbook",
    "UGC_Tracker":                         "ugc-tracker",
    # No skill: Value_Proposition_Jobs_to_be_done, Value_Proposition_Pains_and_Gains,
    #           Hooked_Model, UAC_Tracker
}

SPACES = ["strategy-space", "problem-space", "solution-space", "product-space", "market-space"]


def add_skill_to_frontmatter(filepath, skill_name):
    with open(filepath, encoding="utf-8") as f:
        content = f.read()

    if not content.startswith("---"):
        print(f"  SKIP (no frontmatter): {filepath}")
        return

    end = content.find("\n---", 3)
    if end == -1:
        print(f"  SKIP (unclosed frontmatter): {filepath}")
        return

    fm_block = content[4:end]

    if "skill:" in fm_block:
        print(f"  SKIP (skill already set): {os.path.basename(filepath)}")
        return

    new_fm = fm_block.rstrip("\n") + f"\nskill: {skill_name}\n"
    new_content = "---\n" + new_fm + "---" + content[end + 4:]

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"  OK: {os.path.basename(filepath)} → {skill_name}")


def main():
    updated = 0
    for space in SPACES:
        space_dir = os.path.join(ROOT, space)
        for filename in sorted(os.listdir(space_dir)):
            if not filename.endswith(".md") or filename == "README.md":
                continue
            stem = filename[:-3]
            skill = SKILL_MAP.get(stem)
            if not skill:
                print(f"  NO SKILL: {filename}")
                continue
            skill_path = os.path.join(ROOT, "skills", f"{skill}.md")
            if not os.path.isfile(skill_path):
                print(f"  MISSING SKILL FILE: {skill}.md (for {filename})")
                continue
            add_skill_to_frontmatter(os.path.join(space_dir, filename), skill)
            updated += 1
    print(f"\n✓ Done — {updated} files updated")


if __name__ == "__main__":
    main()
