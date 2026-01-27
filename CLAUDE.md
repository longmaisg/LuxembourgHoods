# LuxembourgHoods

Blogger theme for Luxembourg commune data visualization.

## Token-Saving Rules

1. **NEVER read these large files** (data loaded at runtime from GitHub):
   - `data/external/*.json` - commune data, paths, labels, dimensions
   - `neighborhood-theme.xml.backup` - old backup

2. **Read only when modifying**:
   - `theme.xml` (~30KB) - main theme with HTML/CSS/JS logic

3. **Safe to read** (small files):
   - `CLAUDE.md` - this file
   - `CHANGELOG.md` - git log
   - `data/SOURCES.md` - data sources
   - `data/scripts/*.py` - extraction scripts

## Project Structure

```
theme.xml                    # Main Blogger theme (slim, no data)
data/
  external/                  # JSON data files (hosted on GitHub)
    communes.json            # Commune data with all layers
    paths.json               # SVG paths for map
    labels.json              # Label positions
    dimensions.json          # Data layer definitions
  raw/                       # Original source data (XLS, CSV)
  scripts/                   # Python extraction scripts
commit.sh                    # Quick git commit: ./commit.sh "message"
CHANGELOG.md                 # Git log with anchors
```

## Data Layers

| Key | Label | Format | Source |
|-----|-------|--------|--------|
| price_m2 | Price/m² (Existing) | currency | STATEC |
| price_m2_new | Price/m² (New Build) | currency | STATEC |
| population | Population | number | RNPP |
| area_km2 | Area (km²) | decimal | Cadastre |
| density | Density (pop/km²) | decimal | Calculated |
| foreign_pct | Foreign Population % | percent | RNPP |

## Commands

```bash
./commit.sh "message"        # Commit and push with log
python data/scripts/extract_demographics.py  # Re-extract data
```

## GitHub Raw URLs

Data loaded from:
- https://raw.githubusercontent.com/longmaisg/LuxembourgHoods/master/data/external/communes.json
- https://raw.githubusercontent.com/longmaisg/LuxembourgHoods/master/data/external/paths.json
- https://raw.githubusercontent.com/longmaisg/LuxembourgHoods/master/data/external/labels.json
- https://raw.githubusercontent.com/longmaisg/LuxembourgHoods/master/data/external/dimensions.json
