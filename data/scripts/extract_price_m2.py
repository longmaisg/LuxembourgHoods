#!/usr/bin/env python3
"""
Extract price per m² data from official Luxembourg government XLS file.

Source: Observatoire de l'Habitat / STATEC
URL: https://data.public.lu/en/datasets/prix-de-vente-des-appartements-par-commune/
Data: Average sale prices per m² of apartments by commune (Oct 2024 - Sep 2025)

File structure (after row 9):
- Column 1: Commune name
- Column 2: Number of existing apartment sales
- Column 3: Average price per m² (existing) - number or "*" if <10 transactions
- Column 4: Price range (existing)
- Column 5: Number of VEFA (new construction) sales
- Column 6: Average price per m² (VEFA) - number or "*" if <10 transactions
- Column 7: Price range (VEFA)
"""

import pandas as pd
import json
from pathlib import Path

# Paths
SCRIPT_DIR = Path(__file__).parent
DATA_DIR = SCRIPT_DIR.parent
RAW_FILE = DATA_DIR / "raw" / "prix-m2-commune-2025t3.xls"
OUTPUT_FILE = DATA_DIR / "extracted" / "price_m2.json"

# Commune name normalization to ID
def normalize_to_id(name):
    """Convert commune name to snake_case ID."""
    if not name or not isinstance(name, str):
        return None

    # Special mappings for merged/renamed communes
    special_mappings = {
        "Luxembourg-Ville": "luxembourg",
        "Bous-Waldbredimus": "bous",  # Combined reporting
        "Groussbus-Wal": "grosbous",  # Alternative spelling
        "Habscht": "hobscheid",  # Merged commune
    }

    name = name.strip()
    if name in special_mappings:
        return special_mappings[name]

    # Convert to ID format
    commune_id = (name.lower()
        .replace("é", "e")
        .replace("è", "e")
        .replace("ê", "e")
        .replace("ë", "e")
        .replace("ä", "a")
        .replace("ü", "u")
        .replace("ö", "o")
        .replace("-", "_")
        .replace(" ", "_")
        .replace("'", "")
        .replace("/", "_"))

    return commune_id

def parse_price(value):
    """Parse price value, returns float or None."""
    if pd.isna(value):
        return None
    if isinstance(value, (int, float)):
        return float(value)
    if value == "*":
        return None
    try:
        return float(value)
    except:
        return None

def main():
    print(f"Reading raw data from: {RAW_FILE}")
    print(f"Source: Observatoire de l'Habitat / STATEC")
    print(f"Period: October 2024 - September 2025")
    print("-" * 60)

    # Read the Excel file, skip header rows
    df = pd.read_excel(RAW_FILE, sheet_name=0, header=None, skiprows=10)

    # Columns: 0=empty, 1=commune, 2=n_existing, 3=price_existing, 4=range_existing, 5=n_vefa, 6=price_vefa, 7=range_vefa

    extracted = {}
    skipped = []

    for idx, row in df.iterrows():
        commune_name = row.iloc[1] if len(row) > 1 else None

        # Skip non-commune rows
        if not commune_name or not isinstance(commune_name, str):
            continue
        if commune_name in ["Commune", "Moyenne nationale", "Total des transactions", "Source :"]:
            continue
        if "Précisions" in commune_name or "statistiques" in commune_name.lower():
            continue

        commune_id = normalize_to_id(commune_name)
        if not commune_id:
            continue

        # Parse prices
        n_existing = row.iloc[2] if len(row) > 2 else None
        price_existing = parse_price(row.iloc[3]) if len(row) > 3 else None
        n_vefa = row.iloc[5] if len(row) > 5 else None
        price_vefa = parse_price(row.iloc[6]) if len(row) > 6 else None

        # Use existing price if available, otherwise VEFA
        if price_existing:
            price = price_existing
            price_type = "existing"
            n_transactions = n_existing
        elif price_vefa:
            price = price_vefa
            price_type = "new_construction"
            n_transactions = n_vefa
        else:
            # No price data (less than 10 transactions in both categories)
            skipped.append(commune_name)
            continue

        extracted[commune_id] = {
            "id": commune_id,
            "name": commune_name,
            "price_m2": round(price),
            "price_type": price_type,
            "price_existing": round(price_existing) if price_existing else None,
            "price_vefa": round(price_vefa) if price_vefa else None,
            "n_transactions": int(n_transactions) if pd.notna(n_transactions) else None,
            "period": "Oct 2024 - Sep 2025",
            "source": "Observatoire de l'Habitat / STATEC",
            "source_url": "https://data.public.lu/en/datasets/prix-de-vente-des-appartements-par-commune/"
        }

    print(f"\nExtracted: {len(extracted)} communes with price data")
    print(f"Skipped: {len(skipped)} communes (insufficient transactions)")

    if skipped:
        print(f"\nSkipped communes: {', '.join(skipped[:10])}{'...' if len(skipped) > 10 else ''}")

    # Save extracted data
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(extracted, f, indent=2, ensure_ascii=False)

    print(f"\nExtracted data saved to: {OUTPUT_FILE}")

    # Print sample
    print("\n" + "=" * 60)
    print("Sample extracted data (sorted by price):")
    print("=" * 60)
    sorted_communes = sorted(extracted.values(), key=lambda x: x['price_m2'], reverse=True)
    for c in sorted_communes[:10]:
        print(f"  {c['name']:25} €{c['price_m2']:,}/m² ({c['price_type']})")
    print("  ...")
    for c in sorted_communes[-3:]:
        print(f"  {c['name']:25} €{c['price_m2']:,}/m² ({c['price_type']})")

    return extracted

if __name__ == "__main__":
    main()
