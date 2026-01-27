# LuxembourgHoods

Blogger theme for Luxembourg commune visualization.

## Rules
- NEVER read large files: `data/external/*.json`, `*.backup`
- Read `theme.xml` only when modifying
- Use `./commit.sh "msg"` after changes
- Use uv, never pip

## Structure
- `theme.xml` - Blogger theme (loads data from GitHub)
- `data/external/` - JSON data (communes, paths, labels, dimensions)
- `data/raw/` - source XLS/CSV
- `data/scripts/` - extraction scripts

## Data
Layers: price_m2, price_m2_new, population, area_km2, density, foreign_pct
