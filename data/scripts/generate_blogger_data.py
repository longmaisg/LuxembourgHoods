#!/usr/bin/env python3
"""
Generate COMMUNE_DATA for Blogger theme from extracted data.
Converts extracted JSON data to the format expected by neighborhood-theme.xml
"""

import json
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
DATA_DIR = SCRIPT_DIR.parent
PRICE_FILE = DATA_DIR / "extracted" / "price_m2.json"
OUTPUT_FILE = DATA_DIR / "extracted" / "blogger_commune_data.js"

# Region mapping based on Luxembourg geography
REGION_MAP = {
    # Center
    "luxembourg": "Center", "bertrange": "Center", "strassen": "Center",
    "hesperange": "Center", "sandweiler": "Center", "niederanven": "Center",
    "schuttrange": "Center", "contern": "Center", "weiler_la_tour": "Center",
    "roeser": "Center", "leudelange": "Center", "kopstal": "Center",
    "steinsel": "Center", "walferdange": "Center", "lorentzweiler": "Center",
    "lintgen": "Center", "mersch": "Center", "frisange": "Center",
    "mamer": "Center", "kehlen": "Center", "steinfort": "Center",
    "hobscheid": "Center", "koerich": "Center", "garnich": "Center",
    "dippach": "Center", "reckange_sur_mess": "Center", "mondorf_les_bains": "Center",
    "dalheim": "Center", "junglinster": "Center", "bissen": "Center",
    "colmar_berg": "Center", "helperknapp": "Center",

    # South
    "esch_sur_alzette": "South", "differdange": "South", "dudelange": "South",
    "petange": "South", "sanem": "South", "bettembourg": "South",
    "schifflange": "South", "kaerjeng": "South", "kayl": "South",
    "rumelange": "South", "mondercange": "South",

    # North
    "ettelbruck": "North", "diekirch": "North", "wiltz": "North",
    "clervaux": "North", "weiswampach": "North", "parc_hosingen": "North",
    "erpeldange_sur_sûre": "North", "schieren": "North", "larochette": "North",

    # East (Moselle)
    "grevenmacher": "East", "echternach": "East", "remich": "East",
    "schengen": "East", "wormeldange": "East", "mertert": "East",

    # West
    "redange": "West", "ell": "West", "grosbous": "West",
}

def get_region(commune_id):
    """Get region for a commune."""
    return REGION_MAP.get(commune_id, "Luxembourg")

def main():
    print("Loading extracted price data...")
    with open(PRICE_FILE, 'r', encoding='utf-8') as f:
        price_data = json.load(f)

    print(f"Loaded {len(price_data)} communes")

    # Build COMMUNE_DATA structure
    commune_data = {}

    for commune_id, data in price_data.items():
        commune_data[commune_id] = {
            "id": commune_id,
            "name": data["name"],
            "region": get_region(commune_id),
            "data": {
                "price_m2": {
                    "value": data["price_m2"],
                    "year": 2025,
                    "source": data["source"],
                    "source_url": data["source_url"]
                }
            }
        }

        # Add price_vefa as separate dimension if available
        if data.get("price_vefa"):
            commune_data[commune_id]["data"]["price_m2_new"] = {
                "value": data["price_vefa"],
                "year": 2025,
                "source": data["source"],
                "source_url": data["source_url"]
            }

    # Generate JavaScript output
    js_output = f"""// ============================================
// COMMUNE DATA - Generated from official sources
// Source: Observatoire de l'Habitat / STATEC
// Period: Oct 2024 - Sep 2025
// Generated: {__import__('datetime').datetime.now().strftime('%Y-%m-%d')}
// ============================================
window.COMMUNE_DATA = {json.dumps(commune_data, indent=2, ensure_ascii=False)};
"""

    # Save output
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(js_output)

    print(f"\nGenerated Blogger data saved to: {OUTPUT_FILE}")
    print(f"Total communes: {len(commune_data)}")

    # Print sample
    print("\nSample entries:")
    for i, (k, v) in enumerate(list(commune_data.items())[:3]):
        print(f"  {k}: {v['name']} ({v['region']}) - €{v['data']['price_m2']['value']}/m²")

    return commune_data

if __name__ == "__main__":
    main()
