# LuxembourgHoods - Data-Driven Architecture

## New Concept

**Objective facts only. No opinions. Full source citations.**

User can:
1. View Luxembourg map with commune boundaries
2. Select data layer (population, income, price/m², etc.)
3. See choropleth map (colors showing data intensity)
4. Click any commune to see all facts + sources

---

## Tech Stack Recommendation

### Option A: Static Site (Simple, Free Hosting)
```
Frontend: HTML + Leaflet.js + D3.js
Data: JSON files
Hosting: GitHub Pages / Netlify (free)
```

### Option B: Full App (More Features)
```
Frontend: React/Vue + Leaflet/Mapbox
Backend: Python (FastAPI) or Node.js
Database: SQLite or PostgreSQL
Hosting: Vercel / Railway
```

**Recommendation: Start with Option A**, upgrade later if needed.

---

## Core Components

### 1. Map Library: Leaflet.js (Free, Open Source)
```html
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
```

### 2. Commune Boundaries: GeoJSON
- Source: https://data.public.lu/ (official Luxembourg boundaries)
- Format: GeoJSON polygons for each commune

### 3. Data Layers
Each layer = one JSON file or one property in main data file

| Layer | Data Source | Update Frequency |
|-------|-------------|------------------|
| Population | STATEC | Yearly |
| Avg. Price/m² | Observatoire/Immotop | Monthly |
| Median Income | STATEC | Yearly |
| Foreign Population % | STATEC | Yearly |
| Unemployment Rate | STATEC | Quarterly |
| School Count | Guichet.lu | Yearly |
| Transport Score | Mobiliteit | Static |

---

## File Structure

```
LuxembourgHoods/
├── index.html              # Main map page
├── css/
│   └── style.css
├── js/
│   ├── map.js              # Leaflet map setup
│   ├── layers.js           # Layer switching logic
│   └── commune-detail.js   # Popup/sidebar content
├── data/
│   ├── communes.json       # All commune data with sources
│   ├── boundaries.geojson  # Commune polygons
│   └── SOURCES.md          # Source documentation
└── scripts/
    └── fetch_data.py       # Script to update data from APIs
```

---

## Data Flow

```
1. Government APIs (STATEC, etc.)
         ↓
2. fetch_data.py (Python script)
         ↓
3. communes.json (with source citations)
         ↓
4. Leaflet.js renders map
         ↓
5. User clicks commune → show data + sources
```

---

## Map Layers UI

```
┌─────────────────────────────────────┐
│  [Select Layer ▼]                   │
│   ○ Population                      │
│   ○ Price per m²                    │
│   ○ Median Income                   │
│   ○ Foreign Residents %             │
│   ○ Schools                         │
├─────────────────────────────────────┤
│                                     │
│         LUXEMBOURG MAP              │
│    (choropleth based on layer)      │
│                                     │
│       [Click commune for details]   │
│                                     │
└─────────────────────────────────────┘
```

---

## Commune Detail Panel

When user clicks a commune:

```
┌─────────────────────────────────────┐
│  BELVAUX                    [×]     │
│  Part of Sanem commune              │
├─────────────────────────────────────┤
│  Population         8,234           │
│  Source: STATEC 2024 [↗]            │
│─────────────────────────────────────│
│  Avg. Price/m²      €7,191          │
│  Source: Immotop Nov 2025 [↗]       │
│─────────────────────────────────────│
│  Median Income      €48,500         │
│  Source: STATEC 2023 [↗]            │
│─────────────────────────────────────│
│  ... more facts ...                 │
└─────────────────────────────────────┘
```

Each fact links to its source.

---

## Color Scale (Choropleth)

Use sequential color scale based on data:

- **Low values**: Light color
- **High values**: Dark color

Example for Price/m²:
```
€4,000  →  Light blue
€8,000  →  Medium blue
€12,000 →  Dark blue
```

---

## No Blogger Needed

This new approach is a **web app**, not a blog.

Simple hosting options:
- GitHub Pages (free)
- Netlify (free)
- Vercel (free)

---

## Next Steps

1. [ ] Download commune boundaries GeoJSON from data.public.lu
2. [ ] Fetch real population data from STATEC
3. [ ] Create basic Leaflet map with boundaries
4. [ ] Add layer switching
5. [ ] Add commune click → detail panel
6. [ ] Style and polish

---

## Legal/Ethical Notes

- Always cite sources
- Use government open data when possible (legally safe)
- For real estate data: prefer Observatoire de l'Habitat (government)
- Store source URLs with every data point
- Show "last updated" dates
