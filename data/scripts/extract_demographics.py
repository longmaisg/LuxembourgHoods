#!/usr/bin/env python3
"""Extract demographic data layers from official Luxembourg government sources.

Data sources:
- Population: RNPP via data.public.lu (population-commune-2025.xlsx)
- Area: Administrative limits (commune-area.csv)
- Nationality: RNPP nationality data (nationality-commune-2025.csv)

Outputs layers: population, area_km2, density, foreign_pct
"""

import json
import pandas as pd
from pathlib import Path

BASE = Path(__file__).parent.parent.parent
RAW = BASE / "data" / "raw"
COMMUNES = BASE / "data" / "communes"

# Mapping from official names to our commune IDs
NAME_TO_ID = {
    "Beaufort": None,  # Not in our dataset
    "Bech": None,
    "Beckerich": None,
    "Berdorf": None,
    "Bertrange": "bertrange",
    "Bettembourg": "bettembourg",
    "Bettendorf": None,
    "Betzdorf": None,
    "Bissen": "bissen",
    "Biwer": None,
    "Boulaide": None,
    "Bourscheid": None,
    "Clervaux": "clervaux",
    "Colmar-Berg": "colmar_berg",
    "Consdorf": None,
    "Contern": "contern",
    "Dalheim": "dalheim",
    "Diekirch": "diekirch",
    "Differdange": "differdange",
    "Dippach": "dippach",
    "Dudelange": "dudelange",
    "Echternach": "echternach",
    "Ell": "ell",
    "Erpeldange-sur-Sûre": "erpeldange_sur_sure",
    "Esch-sur-Alzette": "esch_sur_alzette",
    "Esch-sur-Sûre": None,
    "Ettelbruck": "ettelbruck",
    "Feulen": None,
    "Fischbach": None,
    "Flaxweiler": None,
    "Frisange": "frisange",
    "Garnich": None,
    "Goesdorf": None,
    "Grevenmacher": "grevenmacher",
    "Grosbous": "grosbous",
    "Groussbus-Wal": "grosbous",  # Alternative name
    "Habscht": "hobscheid",
    "Heffingen": None,
    "Helperknapp": "helperknapp",
    "Hesperange": "hesperange",
    "Junglinster": "junglinster",
    "Kayl": "kayl",
    "Kehlen": "kehlen",
    "Kiischpelt": None,
    "Koerich": None,
    "Kopstal": "kopstal",
    "Käerjeng": "kaerjeng",
    "Lac de la Haute-Sûre": None,
    "Larochette": "larochette",
    "Lenningen": None,
    "Leudelange": "leudelange",
    "Lintgen": "lintgen",
    "Lorentzweiler": "lorentzweiler",
    "Luxembourg": "luxembourg",
    "Mamer": "mamer",
    "Manternach": None,
    "Mersch": "mersch",
    "Mertert": "mertert",
    "Mertzig": None,
    "Mondercange": "mondercange",
    "Mondorf-les-Bains": "mondorf_les_bains",
    "Niederanven": "niederanven",
    "Nommern": None,
    "Parc Hosingen": "parc_hosingen",
    "Préizerdaul": None,
    "Putscheid": None,
    "Pétange": "petange",
    "Rambrouch": None,
    "Reckange-sur-Mess": "reckange_sur_mess",
    "Redange/Attert": "redange",
    "Reisdorf": None,
    "Remich": "remich",
    "Roeser": "roeser",
    "Rosport-Mompach": None,
    "Rumelange": "rumelange",
    "Saeul": None,
    "Sandweiler": "sandweiler",
    "Sanem": "sanem",
    "Schengen": "schengen",
    "Schieren": "schieren",
    "Schifflange": "schifflange",
    "Schuttrange": "schuttrange",
    "Stadtbredimus": None,
    "Steinfort": "steinfort",
    "Steinsel": "steinsel",
    "Strassen": "strassen",
    "Tandel": None,
    "Troisvierges": None,
    "Useldange": None,
    "Vallée de l'Ernz": None,
    "Vianden": None,
    "Vichten": None,
    "Walferdange": "walferdange",
    "Waldbillig": None,
    "Weiler-la-Tour": "weiler_la_tour",
    "Weiswampach": "weiswampach",
    "Wiltz": "wiltz",
    "Wincrange": None,
    "Winseler": None,
    "Wormeldange": "wormeldange",
    # Alternative spellings from nationality file
    "Colmar - Berg": "colmar_berg",
    "Erpeldange-Sur-Sûre": "erpeldange_sur_sure",
    "Esch-Sur-Alzette": "esch_sur_alzette",
    "Mondorf-Les-Bains": "mondorf_les_bains",
    "Parc-Hosingen": "parc_hosingen",
    "Reckange-Sur-Mess": "reckange_sur_mess",
    "Redange": "redange",
    "Weiler-La-Tour": "weiler_la_tour",
    "Luxembourg-Ville": "luxembourg",
}

SOURCE_INFO = {
    "population": {
        "source": "RNPP / CTIE",
        "source_url": "https://data.public.lu/en/datasets/population-par-commune-population-per-municipality",
        "year": 2025
    },
    "area_km2": {
        "source": "Administration du cadastre et de la topographie",
        "source_url": "https://data.public.lu/en/datasets/limites-administratives-du-grand-duche-de-luxembourg/",
        "year": 2024
    },
    "density": {
        "source": "Calculated from RNPP population and cadastre area",
        "source_url": "https://data.public.lu/",
        "year": 2025
    },
    "foreign_pct": {
        "source": "RNPP / CTIE",
        "source_url": "https://data.public.lu/en/datasets/registre-national-des-personnes-physiques-rnpp-nombre-de-ressortissants-par-nationalite-et-par-commune-number-of-citizens-per-nationality-and-municipality/",
        "year": 2025
    }
}

def normalize_name(name):
    """Normalize commune name for matching."""
    return name.strip().lower().replace("-", " ").replace("  ", " ")

def load_population():
    """Load population data from XLSX."""
    df = pd.read_excel(RAW / "population-commune-2025.xlsx")
    result = {}
    for _, row in df.iterrows():
        name = row['COMMUNE_NOM']
        # Total population = sum of all columns
        total = (row['FEMMES_MINEURES'] + row['HOMMES_MINEURS'] +
                 row['FEMMES_MAJEURES'] + row['HOMMES_MAJEURS'])
        if total > 0:  # Skip entries with 0 population
            result[name] = int(total)
    return result

def load_area():
    """Load area data from CSV (in m², convert to km²)."""
    df = pd.read_csv(RAW / "commune-area.csv")
    result = {}
    for _, row in df.iterrows():
        name = row['COMMUNE']
        area_m2 = row['SURFACE_GEOMETRIQUE_COMMUNE_[m2]']
        area_km2 = round(area_m2 / 1_000_000, 2)
        result[name] = area_km2
    return result

def load_nationality():
    """Load nationality data and calculate foreigner percentage."""
    df = pd.read_csv(RAW / "nationality-commune-2025.csv", encoding='latin-1')

    # Group by commune and sum
    commune_totals = {}
    commune_lux = {}

    for _, row in df.iterrows():
        name = row['COMMUNE_NOM']
        count = row['NOMBRE_TOTAL']
        iso3 = row['NATIONALITE_ISO3']

        if name not in commune_totals:
            commune_totals[name] = 0
            commune_lux[name] = 0

        commune_totals[name] += count
        if iso3 == 'LUX':
            commune_lux[name] += count

    # Calculate foreigner percentage
    result = {}
    for name in commune_totals:
        total = commune_totals[name]
        lux = commune_lux.get(name, 0)
        if total > 0:
            foreign_pct = round((total - lux) / total * 100, 1)
            result[name] = foreign_pct

    return result

def get_commune_id(name):
    """Get our commune ID from official name."""
    # Direct lookup
    if name in NAME_TO_ID:
        return NAME_TO_ID[name]

    # Try normalized matching
    norm = normalize_name(name)
    for official, cid in NAME_TO_ID.items():
        if normalize_name(official) == norm:
            return cid

    return None

def main():
    print("Loading data sources...")

    population = load_population()
    print(f"  Population: {len(population)} communes")

    area = load_area()
    print(f"  Area: {len(area)} communes")

    nationality = load_nationality()
    print(f"  Nationality: {len(nationality)} communes")

    # Build data by commune ID
    all_data = {}
    matched = set()

    # Process population
    for name, pop in population.items():
        cid = get_commune_id(name)
        if cid:
            if cid not in all_data:
                all_data[cid] = {}
            all_data[cid]['population'] = pop
            matched.add(cid)

    # Process area
    for name, km2 in area.items():
        cid = get_commune_id(name)
        if cid:
            if cid not in all_data:
                all_data[cid] = {}
            all_data[cid]['area_km2'] = km2

    # Process nationality/foreign %
    for name, pct in nationality.items():
        cid = get_commune_id(name)
        if cid:
            if cid not in all_data:
                all_data[cid] = {}
            all_data[cid]['foreign_pct'] = pct

    # Calculate density
    for cid, data in all_data.items():
        if 'population' in data and 'area_km2' in data:
            density = round(data['population'] / data['area_km2'], 1)
            data['density'] = density

    print(f"\nMatched {len(all_data)} communes")

    # Update commune JSON files
    print("\nUpdating commune files...")
    updated = 0
    for cid, layers in all_data.items():
        fpath = COMMUNES / f"{cid}.json"
        if fpath.exists():
            commune = json.loads(fpath.read_text())

            for layer, value in layers.items():
                info = SOURCE_INFO[layer]
                commune['data'][layer] = {
                    "value": value,
                    "year": info['year'],
                    "source": info['source'],
                    "source_url": info['source_url']
                }

            fpath.write_text(json.dumps(commune, ensure_ascii=False))
            updated += 1

    print(f"Updated {updated} commune files")

    # Update dimensions.json
    dims_path = BASE / "data" / "dimensions.json"
    dims = json.loads(dims_path.read_text())

    dims['population'] = {"label": "Population", "format": "number"}
    dims['area_km2'] = {"label": "Area (km²)", "format": "decimal"}
    dims['density'] = {"label": "Density (pop/km²)", "format": "decimal"}
    dims['foreign_pct'] = {"label": "Foreign Population %", "format": "percent"}

    dims_path.write_text(json.dumps(dims, indent=2, ensure_ascii=False))
    print("\nUpdated dimensions.json")

    # Print summary
    print("\nData layers added:")
    for layer in ['population', 'area_km2', 'density', 'foreign_pct']:
        count = sum(1 for d in all_data.values() if layer in d)
        print(f"  {layer}: {count} communes")

if __name__ == "__main__":
    main()
